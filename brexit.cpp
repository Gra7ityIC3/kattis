#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int c, p, x, l; cin >> c >> p >> x >> l;
    vector<vi> AL(c + 1);
    vi indeg(c + 1);
    for (int i = 0, a, b; i < p; ++i) {
        cin >> a >> b;
        AL[a].push_back(b);
        AL[b].push_back(a);
        ++indeg[a];
        ++indeg[b];
    }
    queue<int> q; q.push(l);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (u == x) return cout << "leave\n", 0;
        indeg[u] = 0;
        for (int v : AL[u])
            if (indeg[v] && --indeg[v] == AL[v].size() / 2)
                q.push(v);
    }
    return cout << "stay\n", 0;
}
