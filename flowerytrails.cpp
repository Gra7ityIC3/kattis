#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, ans = 0; cin >> n >> m;
    vector<vii> AL(n), p(n);
    for (int i = 0, u, v, w; i < m; ++i) {
        cin >> u >> v >> w;
        AL[u].emplace_back(v, w);
        AL[v].emplace_back(u, w);
    }
    vi dist(n, INF); dist[0] = 0;
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    pq.emplace(0, 0);
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d == dist[u])
            for (auto& [v, w] : AL[u])
                if (d + w < dist[v]) {
                    p[v].clear();
                    p[v].emplace_back(u, w);
                    pq.emplace(dist[v] = d + w, v);
                } else if (d + w == dist[v])
                    p[v].emplace_back(u, w);
    }
    queue<int> q; q.push(n - 1);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (auto& [v, w] : p[u]) {
            if (dist[v]) {
                dist[v] = 0;
                q.push(v);
            }
            ans += w;
        }
    }
    cout << ans * 2 << endl;
    return 0;
}
