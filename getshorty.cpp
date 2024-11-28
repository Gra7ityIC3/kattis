#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, x, y; double f;
    while (cin >> n >> m && n) {
        vector<vector<pair<int, double>>> AL(n);
        for (int i = 0; i < m; ++i) {
            cin >> x >> y >> f;
            AL[x].emplace_back(y, f);
            AL[y].emplace_back(x, f);
        }
        vector<double> dist(n, 0); dist[0] = 1;
        priority_queue<pair<double, int>> pq;
        pq.emplace(1, 0);
        while (true) {
            auto [d, u] = pq.top(); pq.pop();
            if (u == n - 1) { printf("%.4f\n", d); break; }
            if (d == dist[u])
                for (auto& [v, w] : AL[u])
                    if (d * w > dist[v])
                        pq.emplace(dist[v] = d * w, v);
        }
    }
    return 0;
}
