#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int s; cin >> s;
    double lo = 0.0, hi = 18000.0;
    while (hi - lo > 1e-6) {
        double r = (lo + hi) / 2;
        int cnt = 0;
        for (int x = 1; x <= r; ++x)
            cnt += sqrt(r * r - x * x);
        4 * cnt > s ? hi = r : lo = r;
    }
    printf("%f\n", hi);
    return 0;
}
