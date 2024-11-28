#include <bits/stdc++.h>
using namespace std;

char grid[100][101];
int R, C;

int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

void floodfill(int r, int c) {
    if (r < 0 || r >= R || c < 0 || c >= C) return;
    if (grid[r][c] != '-') return;
    grid[r][c] = '#';
    for (int d = 0; d < 4; ++d)
        floodfill(r + dr[d], c + dc[d]);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    for (int i = 1; cin >> R >> C; ++i) {
        for (int r = 0; r < R; ++r)
            cin >> grid[r];
        int ans = 0;
        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c)
                if (grid[r][c] == '-')
                    ++ans, floodfill(r, c);
        printf("Case %d: %d\n", i, ans);
    }
    return 0;
}
