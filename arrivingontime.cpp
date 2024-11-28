#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int, int> iiii;
typedef vector<int> vi;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, s, u, v, t0, p, d; cin >> n >> m >> s;
    vector<vector<iiii>> AL(n + 1);
    for (int i = 0; i < m; ++i) {
        cin >> u >> v >> t0 >> p >> d;
        AL[v].emplace_back(u, t0, p, d);
    }
    vi dist(n); dist[n - 1] = s;
    priority_queue<ii> pq; pq.emplace(s, n - 1);
    while (!pq.empty()) {
        auto [t, u] = pq.top(); pq.pop();
        if (u == 0) { cout << t << endl; return 0; }
        if (t == dist[u])
            for (auto& [v, t0, p, d] : AL[u])
                if (t >= d && t0 <= t - d) {
                    int c = t0 + (t - d - t0) / p * p;
                    if (c > dist[v])
                        pq.emplace(dist[v] = c, v);
                }
    }
    cout << "impossible\n";
}
