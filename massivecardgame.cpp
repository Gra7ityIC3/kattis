#include <bits/stdc++.h>
using namespace std;

int a[100000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, q, l, r; cin >> n;
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a, a + n);
    cin >> q;
    while (q--) {
        cin >> l >> r;
        cout << upper_bound(a, a + n, r) - lower_bound(a, a + n, l) << '\n';
    }
    return 0;
}
