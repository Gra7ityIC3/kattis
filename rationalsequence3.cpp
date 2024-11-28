#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t, k, n, p, q, mask; cin >> t;
    while (t--) {
        cin >> k >> n;
        p = q = 1;
        for (mask = 0x40000000; mask && !(n & mask); mask >>= 1);
        while (mask >>= 1) n & mask ? p += q : q += p;
        printf("%d %d/%d\n", k, p, q);
    }
    return 0;
}
