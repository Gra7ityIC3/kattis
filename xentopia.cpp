#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef tuple<int, int, int> iii;
typedef tuple<ll, int, int, int> iiii;
typedef vector<ll> vi;
typedef vector<vi> vvi;

const ll INF = 1e18;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, k1, k2, u, v, x, c, s, t; cin >> n >> m >> k1 >> k2;
    vector<vector<iii>> AL(n + 1);
    for (int i = 0; i < m; ++i) {
        cin >> u >> v >> x >> c;
        AL[u].emplace_back(v, x, c);
        AL[v].emplace_back(u, x, c);
    }
    cin >> s >> t;
    vector<vvi> dist(n + 1, vvi(k1 + 1, vi(k2 + 1, INF)));
    dist[s][k1][k2] = 0;
    priority_queue<iiii, vector<iiii>, greater<iiii>> pq;
    pq.emplace(0, s, k1, k2);
    while (!pq.empty()) {
        auto [d, u, k1, k2] = pq.top(); pq.pop();
        if (u == t && k1 == 0 && k2 == 0) {
            cout << d << endl;
            return 0;
        }
        if (d == dist[u][k1][k2])
            for (auto& [v, w, c] : AL[u])
                if (c == 0 && d + w < dist[v][k1][k2])
                    pq.emplace(dist[v][k1][k2] = d + w, v, k1, k2);
                else if (c == 1 && k1 && d + w < dist[v][k1 - 1][k2])
                    pq.emplace(dist[v][k1 - 1][k2] = d + w, v, k1 - 1, k2);
                else if (c == 2 && k2 && d + w < dist[v][k1][k2 - 1])
                    pq.emplace(dist[v][k1][k2 - 1] = d + w, v, k1, k2 - 1);
    }
    cout << "-1\n";
}
