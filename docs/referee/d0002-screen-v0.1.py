# D0002 candidate screen v0.1 (Claude, T0008). Exact referee checks for M0008 candidates 1 and 3.
# Run: python3 docs/referee/d0002-screen-v0.1.py   (stdlib only; candidate 2 deliberately not computed)
from fractions import Fraction as F
import itertools
# Candidate 1: rule 150 on an n-ring over GF(2): rank of I+S+S^-1
def rank_gf2(rows):
    rows=rows[:]; r=0; n=len(rows)
    for bit in range(n):
        piv=next((i for i in range(r,n) if rows[i]>>bit&1),None)
        if piv is None: continue
        rows[r],rows[piv]=rows[piv],rows[r]
        for i in range(n):
            if i!=r and rows[i]>>bit&1: rows[i]^=rows[r]
        r+=1
    return r
bad=[]
for n in range(1,61):
    rows=[]
    for i in range(n):
        v=0
        for j in ((i-1)%n,i,(i+1)%n): v^=1<<j
        rows.append(v)
    k=n-rank_gf2(rows)
    if (k!=0)!=(n%3==0) or (n%3==0 and k!=2): bad.append((n,k))
print("C1 rule150: kernel dim = 2 if 3|n else 0, for n=1..60:", "CONFIRMED" if not bad else bad)
# Candidate 3: smallest graph where adding one edge strictly increases hitting time s->t
def hit(n,E,s,t):
    adj={v:set() for v in range(n)}
    for a,b in E: adj[a].add(b); adj[b].add(a)
    V=[v for v in range(n) if v!=t]; idx={v:i for i,v in enumerate(V)}; m=len(V)
    A=[[F(0)]*(m+1) for _ in range(m)]
    for v in V:
        i=idx[v]; d=len(adj[v]); A[i][i]+=1; A[i][m]=F(1)
        for w in adj[v]:
            if w!=t: A[i][idx[w]]-=F(1,d)
    for c in range(m):
        p=next(r for r in range(c,m) if A[r][c]!=0); A[c],A[p]=A[p],A[c]
        A[c]=[x/A[c][c] for x in A[c]]
        for r in range(m):
            if r!=c and A[r][c]!=0: A[r]=[x-A[r][c]*y for x,y in zip(A[r],A[c])]
    return A[idx[s]][m]
def connected(n,E):
    adj={v:set() for v in range(n)}
    for a,b in E: adj[a].add(b); adj[b].add(a)
    seen={0}; st=[0]
    while st:
        v=st.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen)==n
for n in range(2,5):
    pairs=list(itertools.combinations(range(n),2)); found=[]
    for k in range(n-1,len(pairs)+1):
        for E in itertools.combinations(pairs,k):
            if not connected(n,E): continue
            for e in pairs:
                if e in E: continue
                for s in range(n):
                    for t in range(n):
                        if s==t: continue
                        h0,h1=hit(n,E,s,t),hit(n,E+(e,),s,t)
                        if h1>h0: found.append((E,e,s,t,h0,h1))
    print(f"C3 n={n}: witnesses={len(found)}", ("e.g. E=%s add %s s=%d t=%d: %s -> %s"%found[0]) if found else "")
