#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    vector<int> ids[2];
    for (int id = 1, u, v; id <= m; ++id)
        cin >> u >> v, ids[u < v].push_back(id);
    int rem = ids[0].size() >= ids[1].size();
    cout << ids[rem].size() << '\n';
    for (int v : ids[rem]) cout << v << '\n';
    return 0;
}
