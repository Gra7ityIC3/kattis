#include <bits/stdc++.h>
using namespace std;

int dp[1001][1001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1, p; j <= m; ++j) {
            cin >> p;
            dp[i][j] = p + max(dp[i][j-1], dp[i-1][j]);
        }
        cout << dp[i][m] << ' ';
    }
    return 0;
}
