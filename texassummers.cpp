#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n; n += 2;
    vector<ii> points(n);
    vector<vii> AL(n);
    for (auto& [x, y] : points) cin >> x >> y;
    for (int u = 0; u < n; ++u) {
        auto [x1, y1] = points[u];
        for (int v = u + 1; v < n; ++v) {
            auto [x2, y2] = points[v];
            int w = pow(x2 - x1, 2) + pow(y2 - y1, 2);
            AL[u].emplace_back(v, w);
            AL[v].emplace_back(u, w);
        }
    }
    vi dist(n, INF), p(n), ans; dist[n - 2] = 0;
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    pq.emplace(0, n - 2);
    while (true) {
        auto [d, u] = pq.top(); pq.pop();
        if (u == n - 1) break;
        if (d == dist[u])
            for (auto& [v, w] : AL[u])
                if (d + w < dist[v]) {
                    p[v] = u;
                    pq.emplace(dist[v] = d + w, v);
                }
    }
    for (int u = p[n - 1]; u != n - 2; u = p[u])
        ans.push_back(u);
    if (ans.empty())
        cout << "-\n";
    else for (int i = ans.size() - 1; i >= 0; --i)
        cout << ans[i] << '\n';
    return 0;
}
