#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> iii;
typedef vector<int> vi;
typedef vector<iii> viii;

const int INF = 1e9;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, l1, l2, d; char c; cin >> n >> m;
    vector<viii> AL(n + 1);
    for (int i = 0; i < m; ++i) {
        cin >> l1 >> l2 >> d >> c;
        int color = string("ROYGBIV").find(c);
        AL[l1].emplace_back(l2, d, color);
        AL[l2].emplace_back(l1, d, color);
    }
    vector<vi> dist(n + 1, vi(128, INF)); dist[1][0] = 0;
    priority_queue<iii, vector<iii>, greater<iii>> pq;
    pq.emplace(0, 1, 0);
    while (true) {
        auto [d, u, x] = pq.top(); pq.pop();
        if (u == 1 && x == 127) {
            cout << d << endl;
            return 0;
        }
        if (d == dist[u][x])
            for (auto& [v, w, c] : AL[u]) {
                int y = x | 1 << c;
                if (d + w < dist[v][y])
                    pq.emplace(dist[v][y] = d + w, v, y);
            }
    }
}
