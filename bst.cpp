#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    map<int, int> depth;
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        int x, d = 0; cin >> x;
        auto it = depth.lower_bound(x);
        if (it != depth.end()) d = it->second + 1;
        if (it != depth.begin()) d = max(d, (--it)->second + 1);
        depth[x] = d;
        total += d;
        cout << total << '\n';
    }
    return 0;
}
