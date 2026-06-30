#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k; cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        if (k >= x) {
            k -= x;
            cout << 1;
        } else {
            cout << 0;
        }
    }
    return 0;
}
