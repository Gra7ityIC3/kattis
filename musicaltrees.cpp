#include <bits/stdc++.h>
using namespace std;

int n, m, ans;
int p[100], t[100], taken[100];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 0; i < n; ++i) cin >> p[i];
    for (int i = 0; i < m; ++i) cin >> t[i];
    sort(t, t + m);
    for (int i = 0; i < n; ++i) {
        int pos = lower_bound(t, t + m, p[i]) - t;
        pos -= pos == m || pos && t[pos] - p[i] >= p[i] - t[pos - 1];
        ans += taken[pos];
        taken[pos] = 1;
    }
    cout << ans << endl;
    return 0;
}
