#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    vector<int> a(n);
    while (m--) {
        for (int i = n / 2, x; i < n; ++i)
            cin >> x, a[x - 1] |= 1LL << m - 1;
        for (int i = n / 2, x; i < n; ++i)
            cin >> x;
    }
    cout << (unordered_set<int>(a.begin(), a.end()).size() == n ? "YES\n" : "NO\n");
    return 0;
}
