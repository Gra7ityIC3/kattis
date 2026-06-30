#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int k, m;
    while (cin >> k >> m) {
        unordered_set<int> s;
        for (int i = 0; i < k; ++i) {
            int x; cin >> x;
            s.insert(x);
        }
        string ans = "yes";
        for (int i = 0; i < m; ++i) {
            int c, r; cin >> c >> r;
            for (int j = 0; j < c; ++j) {
                int x; cin >> x;
                r -= s.count(x);
            }
            if (r > 0) ans = "no";
        }
        cout << ans << '\n';
    }
    return 0;
}
