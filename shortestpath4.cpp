#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int TC, V, X, Q, v, w, s, t, k; cin >> TC;
    while (TC--) {
        cin >> V; vector<vii> AL(V);
        for (int u = 0; u < V; ++u) {
            cin >> X;
            while (X--) {
                cin >> v >> w;
                AL[u].emplace_back(v, w);
            }
        }
        cin >> Q;
        while (Q--) {
            cin >> s >> t >> k;
            vector<vi> dist(V, vi(k, INF)); dist[s][k - 1] = 0;
            priority_queue<iii, vector<iii>, greater<iii>> pq;
            pq.emplace(0, s, k - 1);
            int ans = -1;
            while (!pq.empty()) {
                auto [d, u, k] = pq.top(); pq.pop();
                if (u == t) { ans = d; break; }
                if (d == dist[u][k] && k)
                    for (auto& [v, w] : AL[u])
                        if (d + w < dist[v][k - 1])
                            pq.emplace(dist[v][k - 1] = d + w, v, k - 1);
            }
            cout << ans << '\n';
        }
        cout << '\n';
    }
    return 0;
}
