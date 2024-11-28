#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k, sum = 0; cin >> n >> k;
    for (int i = 0, x; i < n; ++i)
        cin >> x, sum += __builtin_ctz(x);
    cout << (sum >= k) << endl;
    return 0;
}
