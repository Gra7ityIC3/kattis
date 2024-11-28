#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, q, op, a, b; cin >> n >> q;
    vector<int> x(n + 1);
    for (int i = 1; i <= n; ++i) cin >> x[i];
    while (q--) {
        cin >> op >> a >> b;
        if (op == 1) x[a] = b;
        else cout << abs(x[a] - x[b]) << '\n';
    }
    return 0;
}
