#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k, q, l, r; cin >> n >> k;
    vector<long long> seq(n), prefix(n + 1);
    unordered_map<int, int> freq;

    for (int i = 0; i < k; ++i) {
        int x; cin >> x;
        ++freq[x];
    }

    for (const auto& [jump, count] : freq)
        for (int i = 0; i < n; i += jump)
            seq[i] += count;

    for (int i = 0; i < n; ++i)
        prefix[i + 1] = prefix[i] + seq[i];

    cin >> q;
    while (q--) {
        cin >> l >> r;
        cout << prefix[r + 1] - prefix[l] << '\n';
    }
    return 0;
}
