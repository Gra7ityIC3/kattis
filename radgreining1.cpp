#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, s; cin >> n >> m;
    string ans(n, '?'), section;
    for (int i = 0; i < m; ++i) {
        cin >> s >> section;
        for (int j = 0; j < section.length(); ++j) {
            if (ans[s - 1 + j] != '?' && ans[s - 1 + j] != section[j]) {
                cout << "Villa\n";
                return 0;
            }
            ans[s - 1 + j] = section[j];
        }
    }
    cout << ans << endl;
}
