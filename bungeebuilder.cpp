#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, lo, ans = 0; cin >> n >> lo; 
    int hi = lo;
    for (int i = 1, h; i < n; ++i) {
        cin >> h; lo = min(lo, h);
        if (h >= hi) {
            ans = max(ans, hi - lo);
            hi = lo = h;
        } else {
            ans = max(ans, h - lo);
        }
    }
    cout << ans << endl;
    return 0;
}
