#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, a[25]; cin >> n;
    for (int i = 0; i < n; ++i) cin >> a[i];
    vector<char> valid(1 << n);
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            for (int k = j + 1; k < n; ++k)
                valid[1 << i | 1 << j | 1 << k] = (a[i] ^ a[j] ^ a[k]) == 0;
    int ans = n;
    for (int mask = 0; mask < 1 << n; ++mask)
        if (valid[mask])
            for (int i = 0; i < n; ++i)
                valid[mask | 1 << i] = true;
        else
            ans = min(ans, n - __builtin_popcount(mask));
    cout << ans << endl;
    return 0;
}
