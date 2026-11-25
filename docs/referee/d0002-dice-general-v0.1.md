# D0002 — independent exhaustive search for n = 3…9 (Claude, T0010)

Program: [d0002-dice-general-v0.1.c](d0002-dice-general-v0.1.c). Written independently of GPT-6.2's C++. Different method: it accumulates only U(A,B) while enumerating B, and derives the other five directed win counts from the identity sum(X) = n(n+1)/2 + U(X,Y) + U(X,Z). Enumeration: A contains face 1, and B contains the smallest unused face, so each unordered partition is visited exactly once.

    gcc -O3 -march=native -o /tmp/gen docs/referee/d0002-dice-general-v0.1.c
    for n in 3 4 5 6 7 8 9; do /tmp/gen $n; done      # n=9 took 3 min 37 s on one core

Output (2026-11-25):

    n=3 parts=280 equal=2 | unrestricted: cyclic=5 best=5/9 count=5 | equal-sum: cyclic=2 best=5/9 count=2 | golden bound=5.5623
    n=4 parts=5775 equal=32 | unrestricted: cyclic=13 best=9/16 count=13 | equal-sum: cyclic=6 best=9/16 count=6 | golden bound=9.8885
    n=5 parts=126126 equal=305 | unrestricted: cyclic=1732 best=15/25 count=3 | equal-sum: cyclic=305 best=15/25 count=2 | golden bound=15.4508
    n=6 parts=2858856 equal=4331 | unrestricted: cyclic=10705 best=21/36 count=15 | equal-sum: cyclic=1910 best=21/36 count=8 | golden bound=22.2492
    n=7 parts=66512160 equal=63261 | unrestricted: cyclic=697733 best=29/49 count=28 | equal-sum: cyclic=63261 best=29/49 count=8 | golden bound=30.2837
    n=8 parts=1577585295 equal=1025113 | unrestricted: cyclic=6539451 best=39/64 count=4 | equal-sum: cyclic=604442 best=39/64 count=1 | golden bound=39.5542
    n=9 parts=37978905250 equal=17495345 | unrestricted: cyclic=320055263 best=48/81 count=112 | equal-sum: cyclic=17495345 best=48/81 count=42 | golden bound=50.0608

- n = 6 reproduces every count in GPT-6.2's receipt (4,331 / 1,910 / 8 and 10,705 / 15, optimum 21). The witness A={1,9,10,11,12,14}, B={5,6,7,8,13,18}, C={2,3,4,15,16,17} was checked separately by direct comparison: sums 57/57/57, wins 21/21/21.
- `count` is the number of unordered partitions attaining the optimum. "golden bound" is n²·(√5−1)/2, the upper bound on balanced win counts (Trybuła).
- Partition counts equal C(3n−1, n−1)·C(2n−1, n−1).
