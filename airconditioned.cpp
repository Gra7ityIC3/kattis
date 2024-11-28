#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, cur = 0, ans = 0; cin >> n;
    vector<pair<int, int>> temp(n);
    for (auto& [L, U] : temp) cin >> L >> U;
    sort(temp.begin(), temp.end());
    for (auto [L, U] : temp)
        cur = L > cur ? ++ans, U : min(cur, U);
    cout << ans << endl;
    return 0;
}
