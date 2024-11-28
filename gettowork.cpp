#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

void solve(vvi& towns, int n, int t) {
    vi ans(n + 1);
    for (int i = 1; i <= n; ++i) {
        if (i == t) continue;
        sort(towns[i].begin(), towns[i].end());
        int e = towns[i].size();
        while (e > 0) {
            if (towns[i].empty()) {
                cout << "IMPOSSIBLE\n";
                return;
            }
            int p = towns[i].back(); towns[i].pop_back();
            if (p) e -= p, ++ans[i];
        }
    }
    for (int i = 1; i <= n; ++i)
        cout << ans[i] << ' ';
    cout << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int c, n, t, e, h, p; cin >> c;
    for (int i = 1; i <= c; ++i) {
        cin >> n >> t >> e;
        vvi towns(n + 1);
        for (int j = 0; j < e; ++j) {
            cin >> h >> p;
            towns[h].push_back(p);
        }
        cout << "Case #" << i << ": ";
        solve(towns, n, t);
    }
    return 0;
}
