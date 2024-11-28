#include <bits/stdc++.h>
using namespace std;

int a[100000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        long long n, sum = 0; cin >> n;
        for (int i = 0, w; i < n; ++i) {
            cin >> w; a[i] = 0;
            for (int j = 0, s; j < w; ++j)
                cin >> s, a[i] += s;
        }
        sort(a, a + n);
        for (int i = 0; i < n; ++i)
            sum += a[i] * (n - i);
        printf("%f\n", sum * 1.0 / n);
    }
    return 0;
}
