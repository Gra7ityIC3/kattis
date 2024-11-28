#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, cur = 0, ans = 0; cin >> n;
    vector<pair<int, int>> I(n);
    for (auto& [f, s] : I) cin >> s >> f;
    sort(I.begin(), I.end());
    for (auto [f, s] : I)
        if (cur <= s) cur = f, ++ans;
    cout << ans << endl;
    return 0;
}
