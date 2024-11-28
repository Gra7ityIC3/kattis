#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    long long n, ans = 0, p3 = 1; cin >> n;
    int cnt = __builtin_popcountll(n);
    do {
        if (n & 1) ans += (1LL << --cnt) * p3;
        p3 *= 3;
    } while (n >>= 1);
    cout << ans << endl;
    return 0;
}
