#include <bits/stdc++.h>
using namespace std;

int n; double p, s, v;

double f(double c) {
    return n * pow(log2(n), c * sqrt(2)) / p + s * (1 + 1 / c) / v;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> p >> s >> v; p *= 1e9;
    double lo = 0, hi = 1;
    while (f(hi) < f(hi / 2)) hi *= 2;
    for (int i = 0; i < 50; ++i) {
        double delta = (hi - lo) / 3;
        double m1 = lo + delta;
        double m2 = hi - delta;
        f(m1) > f(m2) ? lo = m1 : hi = m2;
    }
    printf("%f %f\n", f(lo), lo);
    return 0;
}
