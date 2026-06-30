#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m;
    while (cin >> n >> m && n) {
        unordered_set<int> s;
        for (int i = 0; i < n; ++i) {
            int x; cin >> x;
            s.insert(x);
        }
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            int x; cin >> x;
            ans += s.count(x);
        }
        cout << ans << '\n';
    }
    return 0;
}
