#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    vector<long long> fish(n);
    vector<pair<int, int>> shops(m);
    for (auto& w : fish) cin >> w;
    for (auto& [p, x] : shops) cin >> x >> p;
    sort(fish.rbegin(), fish.rend());
    sort(shops.rbegin(), shops.rend());
    long long ans = 0;
    for (int i = 0, j = 0; i < n && j < m; ++i) {
        ans += fish[i] * shops[j].first;
        if (--shops[j].second == 0) ++j;
    }
    cout << ans << endl;
    return 0;
}
