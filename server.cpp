#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, t, ans = 0; cin >> n >> t;
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        if (t < x) break;
        t -= x;
        ++ans;
    }
    cout << ans << endl;
    return 0;
}
