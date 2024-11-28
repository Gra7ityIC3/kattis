#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k, ans = 1; cin >> n >> k;
    for (; n; n -= (n + k - 1) / k) ++ans;
    cout << ans << endl;
    return 0;
}
