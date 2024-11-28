#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

vector<vi> adj;
vi visited, ts;

void toposort(int u) {
    visited[u] = 1;
    for (int v : adj[u])
        if (!visited[v])
            toposort(v);
    ts.push_back(u);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, a, b, d;
    while (cin >> n >> m) {
        vector<vii> AL(n + 1);
        for (int i = 0; i < m; ++i) {
            cin >> a >> b >> d;
            AL[a].emplace_back(b, d);
            AL[b].emplace_back(a, d);
        }

        vi dist(n + 1, INF); dist[2] = 0;
        priority_queue<ii, vector<ii>, greater<ii>> pq;
        pq.emplace(0, 2);
        while (!pq.empty()) {
            auto [d, u] = pq.top(); pq.pop();
            if (d == dist[u])
                for (auto& [v, w] : AL[u])
                    if (d + w < dist[v])
                        pq.emplace(dist[v] = d + w, v);
        }

        adj.assign(n + 1, vi());
        for (int u = 1; u <= n; ++u)
            for (auto& [v, w] : AL[u])
                if (dist[u] > dist[v])
                    adj[u].push_back(v);

        visited.assign(n + 1, 0);
        ts.clear();
        for (int u = 1; u <= n; ++u)
            if (!visited[u])
                toposort(u);

        vi ans(n + 1); ans[1] = 1;
        for (int i = n - 1; i >= 0; --i)
            for (int v : adj[ts[i]])
                ans[v] += ans[ts[i]];

        cout << ans[2] << '\n';
    }
    return 0;
}
