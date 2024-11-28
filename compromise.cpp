#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        int n, m, a[100] = {}; cin >> n >> m;
        for (int i = 0; i < n; ++i) {
            string b; cin >> b;
            for (int j = 0; j < m; ++j)
                a[j] += b[j] - '0';
        }
        for (int i = 0; i < m; ++i)
            cout << (2 * a[i] > n);
        cout << '\n';
    }
    return 0;
}
