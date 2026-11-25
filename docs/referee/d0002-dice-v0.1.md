# D0002 candidate 2 — exact finite search (T0009)

Scope from M0009. Prediction recorded in the operator-visible session before computation: equal 21/36, unrestricted 22/36; Claude's 21/36 for both was known, so not blind. No literature novelty claim.

Compile and execute: `g++ -O3 docs/referee/d0002-dice-v0.1.cpp -o /tmp/dice && /tmp/dice` (GCC-compatible C++). Ran successfully locally in this turn.

```
partitions 2858856 equal 4331
cyclic 1910 optimum 21 count 8 wins 21 21 21 sums 57 57 57
1 9 10 11 12 14
5 6 7 8 13 18
2 3 4 15 16 17
cyclic 10705 optimum 21 count 15 wins 21 21 21 sums 57 57 57
1 9 10 11 12 14
5 6 7 8 13 18
2 3 4 15 16 17
```

Enumeration: A contains face 1, B contains smallest unused face; this visits each unordered partition exactly once. Every strictly cyclic triple has one directed orientation modulo rotation; reversing all three pair comparisons when necessary yields that orientation. All 2,858,856 = C(18,6) C(12,6)/6 partitions are visited. Count each optimal cycle once. Independently checked the witness with Python's direct Cartesian comparisons, partition completeness and sums; wins [21,21,21]. Independent exhaustive enumeration not yet performed.

Structural identity: for a six-face die X, sum(X)=21 + wins(X,Y)+wins(X,Z), because rank equals one plus number of smaller faces. Thus equal sums imply wins(A,B)=wins(B,C)=wins(C,A). Equal expectation does not reduce the finite optimum for this instance. Claude's predictions both hold; GPT's unrestricted prediction fails. This is not a general theorem for other dice sizes. Proposed next question: compare 4- and 8-face cases or derive an extremal construction and bound without enumerating all partitions.
