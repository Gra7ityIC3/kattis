#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 50000;
const double INF = 1e9;

int n;
double xs[MAX_N], ys[MAX_N];

double f(double x) {
    double ans = -INF;
    for (int i = 0; i < n; ++i)
        ans = max(ans, (x - xs[i]) * (x - xs[i]) + ys[i] * ys[i]);
    return ans;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    while (cin >> n && n) {
        double lo = INF, hi = -INF;
        for (int i = 0; i < n; ++i) {
            cin >> xs[i] >> ys[i];
            lo = min(lo, xs[i]);
            hi = max(hi, xs[i]);
        }
        for (int i = 0; i < 50; ++i) {
            double delta = (hi - lo) / 3;
            double m1 = lo + delta;
            double m2 = hi - delta;
            f(m1) > f(m2) ? lo = m1 : hi = m2;
        }
        printf("%f %f\n", lo, sqrt(f(lo)));
    }
    return 0;
}
