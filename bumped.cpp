#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef tuple<ll, int, int> iii;
typedef vector<ll> vi;
typedef vector<ii> vii;

const ll INF = 1e18;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, f, s, t, u, v, w; cin >> n >> m >> f >> s >> t;
    vector<vii> AL(n);
    for (int i = 0; i < m; ++i) {
        cin >> u >> v >> w;
        AL[u].emplace_back(v, w);
        AL[v].emplace_back(u, w);
    }
    for (int i = 0; i < f; ++i) {
        cin >> u >> v;
        AL[u].emplace_back(v, 0);
    }
    vector<vi> dist(n, vi(2, INF)); dist[s][1] = 0;
    priority_queue<iii, vector<iii>, greater<iii>> pq;
    pq.emplace(0, s, 1);
    while (true) {
        auto [d, u, k] = pq.top(); pq.pop();
        if (u == t) { cout << d << endl; return 0; }
        if (d == dist[u][k]) {
            for (auto& [v, w] : AL[u])
                if (w && d + w < dist[v][k])
                    pq.emplace(dist[v][k] = d + w, v, k);
                else if (!w && k && d < dist[v][k - 1])
                    pq.emplace(dist[v][k - 1] = d, v, k - 1);
        }
    }
}
