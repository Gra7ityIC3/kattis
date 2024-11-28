#include <bits/stdc++.h>
using namespace std;

int grid[52][52];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            cin >> grid[i][j];
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (grid[i][j] < min({grid[i + 1][j], grid[i - 1][j],
                                  grid[i][j - 1], grid[i][j + 1]}))
                return cout << "Jebb\n", 0;
    return cout << "Neibb\n", 0;
}
