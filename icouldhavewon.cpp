#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s; cin >> s;
    vector<int> ans;
    for (int k = 1; k <= s.length(); ++k) {
        int n = 0, m = 0, x = 0, y = 0;
        for (char c : s) {
            c == 'A' ? ++x : ++y;
            if (x == k) ++n, x = y = 0;
            else if (y == k) ++m, x = y = 0;
        }
        if (n > m) ans.push_back(k);
    }
    cout << ans.size() << '\n';
    for (int k : ans) cout << k << ' ';
    return 0;
}
