#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k, q, l, r; cin >> n >> k;
    vector<long long> seq(n), prefix(n+1);
    unordered_map<int, int> mp;

    for (int i = 0, x; i < k; ++i)
        cin >> x, ++mp[x];

    for (const auto& [jump, x] : mp)
        for (int i = 0; i < n; i += jump)
            seq[i] += x;

    for (int i = 0; i < n; ++i)
        prefix[i+1] = prefix[i] + seq[i];

    cin >> q;
    while (q--) {
        cin >> l >> r;
        cout << prefix[r+1] - prefix[l] << '\n';
    }
    return 0;
}
