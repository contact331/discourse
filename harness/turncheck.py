"""DISCOURSE turn integrity checks between two Git revisions. Python 3.10+, standard library only.

Usage: python harness/turncheck.py --base <rev> [--head <rev>]
Checks integrity predicates only. It cannot establish who authorized anything (see docs/transport.md).
"""
import argparse
import json
import os
import re
import subprocess
import sys

MSG = re.compile(r"threads/d\d+/messages/m\d+-[a-z0-9.-]+\.md")
SYNC = re.compile(r"sync/S\d+\.md")
TURN = re.compile(r"turns/(t\d+)/turn\.json")


def git(*args):
    return subprocess.check_output(["git", *args], text=True)


def show(rev, path):
    try:
        return git("show", f"{rev}:{path}")
    except subprocess.CalledProcessError:
        return None


def meta(text):
    head = text.split("\n---\n", 1)[0]
    return json.loads(head.split("---\n", 1)[1])


def signoff_only(old, new):
    """True if new = old with one '- [ ] **' box ticked and lines appended."""
    ticked = old.replace("- [ ] **", "- [x] **", 1).rstrip("\n")
    return new.startswith(ticked) and new != old


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--head", default="HEAD")
    a = ap.parse_args()
    rows = []

    def add(ok, check, detail=""):
        rows.append(("PASS" if ok else "FAIL", check, detail))

    diff = [line.split("\t") for line in git("diff", "--name-status", "--no-renames", a.base, a.head).splitlines()]
    added = [p for s, p in diff if s == "A"]
    changed = [(s, p) for s, p in diff if s != "A"]
    turns = sorted({m.group(1) for p in added if (m := TURN.fullmatch(p))})
    kind = "turn" if turns else "sync-only"

    base_msgs = [p for p in git("ls-tree", "-r", "--name-only", a.base).splitlines() if MSG.fullmatch(p)]
    touched = [p for s, p in changed if MSG.fullmatch(p)]
    add(not touched, "integrated letters unchanged", ", ".join(touched) or f"{len(base_msgs)} letters checked")
    add(not any(p.startswith(".github/") for _, p in diff), "no workflow changes", "")

    if kind == "turn":
        bad = []
        for s, p in changed:
            if s == "M" and SYNC.fullmatch(p) and signoff_only(show(a.base, p), show(a.head, p)):
                continue
            bad.append(f"{s} {p}")
        add(not bad, "turn modifies only its own paths (plus an incoming sign-off)", ", ".join(bad))
        add(len(turns) == 1, "exactly one new turn envelope", ", ".join(turns))
    else:
        rows.append(("INFO", "sync-only change", ", ".join(f"{s} {p}" for s, p in changed) or "additions only"))

    for tid in turns:
        t = json.loads(show(a.head, f"turns/{tid}/turn.json"))
        add(t.get("id") == tid, f"{tid}: id matches path")
        prev_id = t.get("previous_turn")
        prev_text = show(a.head, f"turns/{prev_id}/turn.json") if prev_id else None
        add(prev_text is not None, f"{tid}: previous turn {prev_id} exists")
        if prev_text:
            prev = json.loads(prev_text)
            if "expected_next_turn" in prev:
                add(prev["expected_next_turn"] == tid, f"{tid}: expected by {prev_id}", prev["expected_next_turn"])
            if "expected_next_message" in prev:
                add(prev["expected_next_message"] == t["messages"][0], f"{tid}: message expected by {prev_id}", prev["expected_next_message"])
            add(prev.get("next_agent") == t.get("author"), f"{tid}: author is {prev_id}'s next_agent", f"{prev.get('next_agent')} vs {t.get('author')}")
            psync = prev.get("sync")
            if psync:
                ptext = show(a.head, psync) or ""
                add("- [x] **" in ptext and "- [ ] **" not in ptext, f"{tid}: preceding receipt {psync} signed")
        for mid in t.get("messages", []):
            text = show(a.head, f"threads/{t['thread_id']}/messages/{mid}.md")
            add(text is not None and meta(text).get("author") == t.get("author"), f"{tid}: {mid} present, authored by {t.get('author')}")
        for p in t.get("documents", []) + [t.get("sync"), t.get("next_prompt")]:
            if p:
                add(show(a.head, p) is not None, f"{tid}: {p} present")
        bc = t.get("base_commit")
        if bc:
            ok = subprocess.run(["git", "merge-base", "--is-ancestor", bc, a.head], capture_output=True).returncode == 0
            add(ok, f"{tid}: base_commit {bc[:12]} is an ancestor")

    width = max(len(r[1]) for r in rows)
    lines = [f"turncheck {kind}: base {a.base[:12]} head {git('rev-parse', a.head).strip()[:12]}"]
    lines += [f"{s:4}  {c:<{width}}  {d}".rstrip() for s, c, d in rows]
    print("\n".join(lines))
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
            f.write("```\n" + "\n".join(lines) + "\n```\n")
    sys.exit(1 if any(r[0] == "FAIL" for r in rows) else 0)


if __name__ == "__main__":
    main()
