#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, t, ans = 0; cin >> n >> t;
    for (int i = 0, x; i < n; ++i) {
        cin >> x; t -= x;
        if (t < 0) break;
        ++ans;
    }
    cout << ans << endl;
    return 0;
}
