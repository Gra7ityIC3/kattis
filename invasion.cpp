#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, a, k, t1, t2, d, b;
    while (cin >> n >> m >> a >> k && n) {
        vector<vii> AL(n + 1);
        for (int i = 0; i < m; ++i) {
            cin >> t1 >> t2 >> d;
            AL[t1].emplace_back(t2, d);
            AL[t2].emplace_back(t1, d);
        }
        vi dist(n + 1, INF);
        for (int i = 0; i < a; ++i) {
            cin >> b; dist[b] = 0;
            priority_queue<ii, vector<ii>, greater<ii>> pq;
            pq.emplace(0, b);
            while (!pq.empty()) {
                auto [d, u] = pq.top(); pq.pop();
                if (d == dist[u])
                    for (auto& [v, w] : AL[u])
                        if (d + w < dist[v])
                            pq.emplace(dist[v] = d + w, v);
            }
            int ans = 0;
            for (int i = 1; i <= n; ++i)
                ans += dist[i] >= k;
            cout << ans << '\n';
        }
        cout << '\n';
    }
    return 0;
}
