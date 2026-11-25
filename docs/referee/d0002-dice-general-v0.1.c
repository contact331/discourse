/* Independent exhaustive search (Claude, T0010). Three n-sided dice partitioning {1..3n}.
   Uses sum(X) = n(n+1)/2 + U(X,Y) + U(X,Z): only U(A,B) is accumulated; others follow. */
#include <stdio.h>
#include <stdlib.h>
static int n, N, T, N2, total;
static int A[16], rem[32], nrem, cA[32];           /* cA[v] = #a in A with a > v (values 1..3n) */
static long long parts, eq, cyc, cycEq; static int best, bestEq; static long long nbest, nbestEq;
static int SA;
static void leaf(int SB, int uAB){
  int SC = total - SA - SB; parts++;
  int uBA = N2 - uAB, uAC = SA - T - uAB, uCA = N2 - uAC, uBC = SB - T - uBA, uCB = N2 - uBC;
  int m = -1;
  if (2*uAB > N2 && 2*uBC > N2 && 2*uCA > N2) { m = uAB; if (uBC<m) m=uBC; if (uCA<m) m=uCA; }
  else if (2*uBA > N2 && 2*uCB > N2 && 2*uAC > N2) { m = uBA; if (uCB<m) m=uCB; if (uAC<m) m=uAC; }
  int isEq = (SA == SB && SB == SC);
  if (isEq) eq++;
  if (m >= 0) {
    cyc++; if (m > best) { best = m; nbest = 0; } if (m == best) nbest++;
    if (isEq) { cycEq++; if (m > bestEq) { bestEq = m; nbestEq = 0; } if (m == bestEq) nbestEq++; }
  }
}
static void chooseB(int start, int left, int SB, int uAB){
  if (!left) { leaf(SB, uAB); return; }
  for (int i = start; i <= nrem - left; i++) chooseB(i+1, left-1, SB + rem[i], uAB + cA[rem[i]]);
}
static void chooseA(int next, int k, int s){
  if (k == n) {
    SA = s; int inA[32] = {0}; for (int i=0;i<n;i++) inA[A[i]] = 1;
    nrem = 0; for (int v=1; v<=N; v++) if (!inA[v]) rem[nrem++] = v;
    for (int v=1; v<=N; v++){ int c=0; for (int i=0;i<n;i++) if (A[i] > v) c++; cA[v]=c; }
    chooseB(1, n-1, rem[0], cA[rem[0]]);   /* B contains the smallest unused face */
    return;
  }
  for (int v = next; v <= N - (n-k) + 1; v++) { A[k] = v; chooseA(v+1, k+1, s+v); }
}
int main(int argc, char **argv){
  n = atoi(argv[1]); N = 3*n; T = n*(n+1)/2; N2 = n*n; total = N*(N+1)/2;
  best = bestEq = -1; A[0] = 1;                    /* A contains face 1 */
  chooseA(2, 1, 1);
  printf("n=%d parts=%lld equal=%lld | unrestricted: cyclic=%lld best=%d/%d count=%lld | equal-sum: cyclic=%lld best=%d/%d count=%lld | golden bound=%.4f\n",
    n, parts, eq, cyc, best, N2, nbest, cycEq, bestEq, N2, nbestEq, 0.6180339887*N2);
  return 0;
}
