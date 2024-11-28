#include <bits/stdc++.h>
using namespace std;

char grid[51][52];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    queue<pair<int, int>> q;
    for (int r = 0; r < n; ++r) {
        cin >> grid[r] + 1;
        for (int c = 1; c <= m; ++c)
            if (grid[r][c] == 'V')
                q.emplace(r, c);
    }
    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        if (grid[r + 1][c] == '.') {
            grid[r + 1][c] = 'V';
            q.emplace(r + 1, c);
        } else if (grid[r + 1][c] == '#') {
            for (int nc : {c - 1, c + 1})
                if (grid[r][nc] == '.') {
                    grid[r][nc] = 'V';
                    q.emplace(r, nc);
                }
        }
    }
    for (int r = 0; r < n; ++r)
        cout << grid[r] + 1 << '\n';
    return 0;
}
