#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    vector<int> t(n);
    for (int i = 0; i < n; ++i) cin >> t[i];
    ll lo = 0, hi = 1e18;
    while (lo < hi) {
        ll mid = (lo + hi) / 2;
        ll sum = 0;
        for (int i = 0; i < n && sum <= m; ++i)
            sum += mid / t[i];
        sum > m ? hi = mid : lo = mid + 1;
    }
    cout << hi << endl;
    return 0;
}
