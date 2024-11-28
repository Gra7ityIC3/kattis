#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, ans = 0; cin >> n;
    vector<int> a(n + 1);
    for (int i = 0, h; i < n; ++i) {
        cin >> h;
        a[h] ? --a[h] : ++ans;
        ++a[h - 1];
    }
    cout << ans << endl;
    return 0;
}
