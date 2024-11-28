#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    vector<pair<int, int>> a(n);
    for (auto& [p, c] : a) cin >> p >> c;
    sort(a.begin(), a.end());
    long long ans = a[n-1].second;
    for (int i = 1; i < n; ++i)
        ans += max(0, a[i-1].second - a[i].second);
    cout << ans << endl;
    return 0;
}
