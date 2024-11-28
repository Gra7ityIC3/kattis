#include <bits/stdc++.h>
using namespace std;

#include <bits/extc++.h>
using namespace __gnu_pbds;

typedef pair<int, int> ii;
typedef tree<ii, null_type, greater_equal<ii>, rb_tree_tag, tree_order_statistics_node_update> ost;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    ost tree;
    unordered_map<int, ii> team;
    for (int i = 0, t, p; i < m; ++i) {
        cin >> t >> p;
        auto& [a, b] = team[t];
        tree.erase(tree.find_by_order(tree.order_of_key({a, b})));
        tree.insert({++a, b -= p});
        cout << tree.order_of_key(team[1]) + 1 << '\n';
    }
    return 0;
}
