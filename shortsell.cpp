#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k, ans = 0, best = 0; cin >> n >> k;
    for (int i = 0, x; i < n; ++i) {
        cin >> x; x *= 100;
        best = max(best - k, x);
        ans = max(ans, best - x - k);
    }
    cout << ans << endl;
    return 0;
}
