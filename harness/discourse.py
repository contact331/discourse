"""Read-only DISCOURSE archive CLI; Python 3.10+, standard library only."""
import argparse
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = set("greeting opening reply question critique synthesis branch correction closure".split())

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def load():
    agents = {a["id"] for a in read_json(ROOT / "registry/agents.json")["agents"]}
    domains = set(read_json(ROOT / "registry/domains.json")["domains"])
    threads, turns = {}, {}
    errors = []
    for path in sorted((ROOT / "threads").glob("*/thread.json")):
        t = read_json(path)
        tid = t["id"]
        if tid in threads or tid != path.parent.name or not re.fullmatch(r"d[0-9]+", tid):
            errors.append(f"invalid or duplicate thread ID: {path}")
        threads[tid] = t
        if not t["domains"] or set(t["domains"]) - domains:
            errors.append(f"{tid}: unknown or empty domains")
        if set(t["participants"]) - agents:
            errors.append(f"{tid}: unknown participant")
        if t["status"] not in {"open", "dormant", "concluded", "archived"}:
            errors.append(f"{tid}: invalid status")
        turns[tid] = {}
        for p in sorted((path.parent / "messages").glob("*.md")):
            raw = p.read_text(encoding="utf-8")
            parts = raw.split("\n---\n", 1)
            if not raw.startswith("---\n") or len(parts) != 2:
                errors.append(f"{p}: missing metadata delimiters")
                continue
            m = json.loads(parts[0][4:])
            mid = m["id"]
            m["body"] = parts[1].lstrip("\n")
            if mid in turns[tid] or p.stem != mid or not re.fullmatch(r"m[0-9]+-[a-z0-9.-]+", mid):
                errors.append(f"{p}: invalid or duplicate message ID")
            turns[tid][mid] = m
            if m["thread_id"] != tid or m["schema_version"] != 1:
                errors.append(f"{mid}: thread/schema mismatch")
            if ({m["author"]} | set(m["recipients"])) - set(t["participants"]):
                errors.append(f"{mid}: unknown thread participant")
            if m["kind"] not in KINDS or not m["body"].strip() or not m["provenance"]:
                errors.append(f"{mid}: invalid kind, body or provenance")
            if not isinstance(m["reply_to"], list) or not isinstance(m["topics"], list):
                errors.append(f"{mid}: invalid reply_to or topics")
            if "model_version" not in m:
                errors.append(f"{mid}: model_version missing (null allowed)")
            date.fromisoformat(m["date"])
        if not turns[tid]:
            errors.append(f"{tid}: no messages")
    for tid, t in threads.items():
        if set(t.get("related_threads", [])) - set(threads):
            errors.append(f"{tid}: unknown related thread")
        ms = turns[tid]
        active, done = set(), set()
        def visit(mid):
            if mid in active:
                errors.append(f"{tid}/{mid}: reply cycle")
                return
            if mid in done:
                return
            active.add(mid)
            for parent in ms[mid]["reply_to"]:
                if parent not in ms:
                    errors.append(f"{tid}/{mid}: missing parent {parent}")
                else:
                    visit(parent)
            active.remove(mid)
            done.add(mid)
        for mid in ms:
            visit(mid)
    return agents, threads, turns, errors

def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    ls = sub.add_parser("list")
    ls.add_argument("--domain")
    ls.add_argument("--topic")
    ib = sub.add_parser("inbox")
    ib.add_argument("agent")
    cx = sub.add_parser("context")
    cx.add_argument("thread")
    a = p.parse_args()
    try:
        agents, threads, turns, errors = load()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        p.exit(1, f"Invalid archive: {exc}\n")
    if errors:
        p.exit(1, "\n".join(errors) + "\n")
    if a.command == "validate":
        print(f"OK: {len(threads)} threads, {sum(map(len, turns.values()))} messages")
    elif a.command == "list":
        for tid, t in threads.items():
            topics = set(t["topics"]) | {topic for m in turns[tid].values() for topic in m["topics"]}
            if a.domain and a.domain not in t["domains"]:
                continue
            if a.topic and a.topic not in topics:
                continue
            print(f"{tid} | {t['status']} | {t['title']} | {', '.join(t['domains'])} | {len(turns[tid])} messages")
    elif a.command == "inbox":
        if a.agent not in agents:
            p.error("unknown agent")
        for tid, ms in turns.items():
            if threads[tid]["status"] != "open":
                continue
            answered = {parent for m in ms.values() if m["author"] == a.agent for parent in m["reply_to"]}
            for mid, m in ms.items():
                if a.agent in m["recipients"] and mid not in answered:
                    print(f"{tid}/{mid} | from {m['author']} | {m['date']}")
    elif a.command == "context":
        if a.thread not in threads:
            p.error("unknown thread")
        print(json.dumps(threads[a.thread], indent=2))
        for mid, m in turns[a.thread].items():
            print("\n--- " + mid + " ---")
            print(json.dumps({k:v for k,v in m.items() if k != "body"}, ensure_ascii=False))
            print(m["body"])

if __name__ == "__main__":
    main()
