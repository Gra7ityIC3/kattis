#include <bits/stdc++.h>
using namespace std;

int u[1000], s[1000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int p; cin >> p;
    while (p--) {
        int k, n, m = 0; cin >> k >> n;
        for (int i = 0; i < n; ++i)
            cin >> u[i], s[i] = u[i];
        sort(s, s + n);
        for (int i = 0; i < n; ++i)
            m += s[m] == u[i];
        printf("%d %d\n", k, n - m);
    }
    return 0;
}
