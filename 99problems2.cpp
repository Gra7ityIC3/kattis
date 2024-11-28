#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, q, t, d; cin >> n >> q;
    map<int, int> mp;
    for (int i = 0; i < n; ++i)
        cin >> d, ++mp[d];
    while (q--) {
        cin >> t >> d;
        auto it = mp.upper_bound(d);
        if (t == 1) {
            if (it == mp.end()) {
                cout << "-1\n";
            } else {
                cout << it->first << '\n';
                if (--it->second == 0) mp.erase(it->first);
            }
        } else if (it == mp.begin()) {
            cout << "-1\n";
        } else {
            cout << (--it)->first << '\n';
            if (--it->second == 0) mp.erase(it->first);
        }
    }
    return 0;
}
