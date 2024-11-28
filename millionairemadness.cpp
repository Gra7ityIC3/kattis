#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> iii;

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, -1, 0, 1};

int grid[1001][1001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int m, n, ans = 0; cin >> m >> n;
    for (int r = 1; r <= m; ++r)
        for (int c = 1; c <= n; ++c)
            cin >> grid[r][c];
    priority_queue<iii, vector<iii>, greater<iii>> pq;
    pq.emplace(0, 1, 1);
    while (true) {
        auto [d, r, c] = pq.top(); pq.pop();
        ans = max(ans, d);
        if (r == m && c == n) break;
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (nr < 1 || nr > m || nc < 1 || nc > n) continue;
            if (grid[nr][nc] == -1) continue;
            pq.emplace(grid[nr][nc] - grid[r][c], nr, nc);
        }
        grid[r][c] = -1;
    }
    cout << ans << endl;
    return 0;
}
