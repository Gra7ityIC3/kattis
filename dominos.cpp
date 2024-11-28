#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

vector<vi> AL;
vi visited, ts;

void toposort(int u) {
    visited[u] = 1;
    for (int v : AL[u])
        if (!visited[v])
            toposort(v);
    ts.push_back(u);
}

void dfs(int u) {
    visited[u] = 1;
    for (int v : AL[u])
        if (!visited[v])
            dfs(v);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        int n, m, ans = 0; cin >> n >> m;
        AL.assign(n + 1, vi());
        for (int i = 0, x, y; i < m; ++i)
            cin >> x >> y, AL[x].push_back(y);
        visited.assign(n + 1, 0);
        ts.clear();
        for (int u = 1; u <= n; ++u)
            if (!visited[u])
                toposort(u);
        visited.assign(n + 1, 0);
        for (int i = n - 1; i >= 0; --i)
            if (!visited[ts[i]])
                ++ans, dfs(ts[i]);
        cout << ans << '\n';
    }
    return 0;
}
