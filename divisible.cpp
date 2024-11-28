#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int c; cin >> c;
    while (c--) {
        int d, n, ans = 0; cin >> d >> n;
        unordered_map<int, int> cnt{{0, 1}};
        for (int i = 0, sum = 0, x; i < n; ++i)
            cin >> x, ans += cnt[sum = (sum + x) % d]++;
        cout << ans << '\n';
    }
    return 0;
}
