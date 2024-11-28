#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    for (int k; cin >> k;) {
        string ans;
        for (; k; k /= 7) ans += "0125986"[k % 7];
        cout << ans << '\n';
    }
    return 0;
}
