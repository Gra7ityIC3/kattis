#include <bits/stdc++.h>
using namespace std;

const int MAX_V = 4000;
const int MOD = 1e9 + 7;

bool g[MAX_V][MAX_V];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int v, e, q; cin >> v >> e >> q;
    for (int i = 0, a, b; i < e; ++i)
        cin >> a >> b, g[a][b] = true;
    bool tp = false, comp = false;
    while (q--) {
        int op, x, y; cin >> op;
        switch (op) {
            case 1:
                if (comp)
                    for (int u = 0; u <= v; ++u)
                        g[u][v] = g[v][u] = true;
                ++v;
                break;
            case 2:
            case 4:
                cin >> x >> y;
                (tp ? g[y][x] : g[x][y]) ^= true;
                break;
            case 3:
                cin >> x;
                for (int y = 0; y < v; ++y)
                    g[y][x] = g[x][y] = comp;
                break;
            case 5:
                tp = !tp;
                break;
            case 6:
                comp = !comp;
                break;
        }
    }
    cout << v << '\n';
    for (int i = 0; i < v; ++i) {
        int h = 0, d = 0;
        for (int j = v - 1; j >= 0; --j) {
            if (i == j || tp && g[j][i] == comp || !tp && g[i][j] == comp)
                continue;
            h = (7LL * h + j) % MOD;
            ++d;
        }
        cout << d << ' ' << h << '\n';
    }
    return 0;
}
