#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int g, n, cur = 0, ans = 0; cin >> g >> n;
    vector<pair<int, int>> tasks(n);
    for (auto& [t_end, t_start] : tasks)
        cin >> t_start >> t_end;
    sort(tasks.begin(), tasks.end());
    for (auto [t_end, t_start] : tasks)
        if (cur <= t_start) cur = t_end, ++ans;
    cout << (ans >= g ? "YES\n" : "NO\n");
    return 0;
}
