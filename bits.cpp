#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        int x, ans = 0; cin >> x;
        while (x) {
            ans = max(ans, __builtin_popcount(x));
            x /= 10;
        }
        cout << ans << '\n';
    }
    return 0;
}
