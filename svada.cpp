#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 100;

int t, n, m;
int a[MAX_N], b[MAX_N], c[MAX_N], d[MAX_N];

bool can(int s) {
    int x = 0, y = 0;
    for (int i = 0; i < n; ++i)
        x += s < a[i] ? 0 : (s - a[i]) / b[i] + 1;
    for (int i = 0; i < m; ++i)
        y += t - s < c[i] ? 0 : (t - s - c[i]) / d[i] + 1;
    return x <= y;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> t >> n;
    for (int i = 0; i < n; ++i) cin >> a[i] >> b[i];
    cin >> m;
    for (int i = 0; i < m; ++i) cin >> c[i] >> d[i];
    int lo = 1, hi = t;
    while (hi - lo > 1) {
        int mid = (lo + hi) / 2;
        can(mid) ? lo = mid : hi = mid;
    }
    cout << lo << endl;
    return 0;
}
