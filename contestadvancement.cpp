#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k, c; cin >> n >> k >> c;
    vector<pair<int, int>> teams(n);
    vector<int> cnt(n + 1);
    for (auto& [t, s] : teams) {
        cin >> t >> s;
        if (cnt[s] < c && k) ++cnt[s], --k;
    }
    for (auto& [t, s] : teams)
        if (--cnt[s] >= 0 || --k >= 0)
            cout << t << '\n';
    return 0;
}
