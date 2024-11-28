#include <bits/stdc++.h>
using namespace std;

double a[10000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t, n, f, r; cin >> t;
    while (t--) {
        cin >> n >> f;
        double lo = 0.0, hi = 0.0;
        for (int i = 0; i < n; ++i) {
            cin >> r;
            a[i] = M_PI * r * r;
            hi = max(hi, a[i]);
        }
        while (hi - lo > 1e-3) {
            double mid = (lo + hi) / 2;
            int cnt = 0;
            for (int i = 0; i < n; ++i)
                cnt += int(a[i] / mid);
            cnt > f ? lo = mid : hi = mid;
        }
        printf("%f\n", lo);
    }
}
