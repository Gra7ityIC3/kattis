#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    vector<int> state(1000000, 3);
    for (int i = 1; i <= 2; ++i) {
        int k; cin >> k;
        while (k--) { int v; cin >> v; state[v] &= i; }
    }
    int ans = 0, disl = 0;
    for (int s : state) if (s < 3 && !(s&disl)) ++ans, disl = s;
    cout << ans << endl;
    return 0;
}
