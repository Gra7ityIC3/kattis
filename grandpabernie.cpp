#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, y, q, k; string s; cin >> n;
    unordered_map<string, vector<int>> mp;
    for (int i = 0, y; i < n; ++i) {
        cin >> s >> y;
        mp[s].push_back(y);
    }
    for (auto& [k, v] : mp)
        sort(v.begin(), v.end());
    cin >> q;
    while (q--) {
        cin >> s >> k;
        cout << mp[s][k - 1] << '\n';
    }
    return 0;
}
