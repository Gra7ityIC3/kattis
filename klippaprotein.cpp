#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string p; int k; cin >> p >> k;
    int n = p.length(), ans = n;
    for (char c : p) {
        int cuts = 0;
        for (int i = 0, j = -k; i < n; ++i)
            if (i - j + 1 > k && p[i] != c)
                ++cuts, j = i;
        ans = min(ans, cuts);
    }
    cout << ans << endl;
    return 0;
}
