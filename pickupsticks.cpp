#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, a, b; cin >> n >> m;
    vector<vector<int>> AL(n + 1);
    vector<int> indeg(n + 1), toposort;
    for (int i = 0; i < m; ++i) {
        cin >> a >> b;
        AL[a].push_back(b);
        ++indeg[b];
    }
    queue<int> q;
    for (int v = 1; v <= n; ++v)
        if (indeg[v] == 0) q.push(v);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        toposort.push_back(u);
        for (int v : AL[u])
            if (--indeg[v] == 0) q.push(v);
    }
    if (toposort.size() == n)
        for (int v : toposort)
            cout << v << '\n';
    else cout << "IMPOSSIBLE\n";
    return 0;
}
