#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        int n, ans = 1; cin >> n;
        for (; abs(n) % 10 != 7; n -= 7) ++ans;
        cout << (n >= 0 ? ans : -1) << '\n';
    }
    return 0;
}
