#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

void radixSort(vi& a, int n) {
    int d = 16, w = 32;
    for (int p = 0; p < w / d; ++p) {
        vi c(1 << d), b(n);
        for (int i = 0; i < n; ++i)
            ++c[(a[i] >> d * p) & ((1 << d) - 1)];
        for (int i = 1; i < 1 << d; ++i)
            c[i] += c[i - 1];
        for (int i = n - 1; i >= 0; --i)
            b[--c[(a[i] >> d * p) & ((1 << d) - 1)]] = a[i];
        a = b;
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int tc; cin >> tc;
    while (tc--) {
        long long n, a, b, c, x, y, v = 0;
        cin >> n >> a >> b >> c >> x >> y;
        vi s(n); s[0] = a;
        for (int i = 1; i < n; ++i)
            s[i] = (s[i - 1] * b + a) % c;
        radixSort(s, n);
        for (int i = 0; i < n; ++i)
            v = (v * x + s[i]) % y;
        cout << v << '\n';
    }
    return 0;
}
