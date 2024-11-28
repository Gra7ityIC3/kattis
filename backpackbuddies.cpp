#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, knight = 0, day = 0; cin >> n >> m;
    vector<vii> AL(n + 1);
    for (int i = 0, u, v, d; i < m; ++i) {
        cin >> u >> v >> d;
        AL[u].emplace_back(v, d);
        AL[v].emplace_back(u, d);
    }
    vi dist(n, INF); dist[0] = 0;
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    pq.emplace(0, 0);
    while (true) {
        auto [d, u] = pq.top(); pq.pop();
        if (u == n - 1) {
            knight = max(0, (d - 1) / 12) * 12 + d;
            break;
        }
        if (d == dist[u])
            for (auto& [v, w] : AL[u])
                if (d + w < dist[v])
                    pq.emplace(dist[v] = d + w, v);
    }
    dist.assign(n, INF); dist[0] = 0;
    pq = {}; pq.emplace(0, 0);
    while (true) {
        auto [d, u] = pq.top(); pq.pop();
        if (u == n - 1) {
            day = max(0, (d - 1) / 12) * 12 + d;
            break;
        }
        if (d == dist[u])
            for (auto [v, w] : AL[u]) {
                if (d % 12 + w > 12) w += 12 - d % 12;
                if (d + w < dist[v])
                    pq.emplace(dist[v] = d + w, v);
            }
    }
    cout << day - knight << endl;
    return 0;
}
