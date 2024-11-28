#include <bits/stdc++.h>
using namespace std;

typedef pair<int, long long> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int A, H, n, m, e, b, a, h; cin >> A >> H >> n >> m;
    vector<vii> AL(n + 1);
    for (int i = 0; i < m; ++i) {
        cin >> e >> b >> a >> h;
        AL[e].emplace_back(b, (h - 1LL) / A * a);
    }
    vi dist(n + 1); dist[1] = H;
    priority_queue<ii> pq; pq.emplace(H, 1);
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (u == n) { cout << d << endl; return 0; }
        if (d == dist[u])
            for (auto& [v, w] : AL[u])
                if (d > w && d - w > dist[v])
                    pq.emplace(dist[v] = d - w, v);
    }
    cout << "Oh no\n";
}
