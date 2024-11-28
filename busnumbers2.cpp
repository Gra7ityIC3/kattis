#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int m, ans = 0; cin >> m;
    unordered_set<int> s;
    for (int i = 1; i <= 73; ++i)
        for (int j = i; j <= 73; ++j) {
            int x = i * i * i + j * j * j;
            if (x > m) break;
            if (!s.insert(x).second) ans = max(ans, x);
        }
    if (ans) cout << ans << endl;
    else cout << "none\n";
    return 0;
}
