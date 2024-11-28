#include <bits/stdc++.h>
using namespace std;

int a[100001], sum[100001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        int n, m, ans = 0; cin >> n >> m;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            sum[i] = sum[i - 1] + a[i];
        }
        for (int i = 1; i <= n; ++i) if (a[i] == m) {
            int left = i, right = i;
            while (left > 1 && a[left - 1] > a[i]) --left;
            while (right < n && a[right + 1] > a[i]) ++right;
            ans = max(ans, sum[right] - sum[left - 1]);
        }
        cout << ans << '\n';
    }
    return 0;
}
