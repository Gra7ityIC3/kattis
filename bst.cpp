#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    map<int, int> depth;
    long long ans = 0;
    for (int i = 0, x; i < n; ++i) {
        cin >> x; auto it = depth.lower_bound(x);
        int d = 0;
        if (it != depth.end()) d = it->second + 1;
        if (it != depth.begin()) d = max(d, (--it)->second + 1);
        depth[x] = d;
        ans += d;
        cout << ans << '\n';
    }
    return 0;
}
