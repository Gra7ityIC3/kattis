#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k; cin >> n >> k;
    vector<bool> sieve(n);
    for (int i = 2; i <= n; ++i) {
        if (sieve[i]) continue;
        for (int j = i; j <= n; j += i) {
            if (sieve[j]) continue;
            if (--k == 0) {
                cout << j << endl;
                return 0;
            }
            sieve[j] = true;
        }
    }
}
