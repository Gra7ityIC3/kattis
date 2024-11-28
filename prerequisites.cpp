#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int k, m;
    while (cin >> k >> m) {
        unordered_set<int> s;
        for (int i = 0, x; i < k; ++i)
            cin >> x, s.insert(x);
        string ans = "yes\n";
        for (int i = 0, c, r; i < m; ++i) {
            cin >> c >> r;
            for (int j = 0, x; j < c; ++j)
                cin >> x, r -= s.count(x);
            if (r > 0) ans = "no\n";
        }
        cout << ans;
    }
    return 0;
}
