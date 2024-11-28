#include <bits/stdc++.h>
using namespace std;

#include <bits/extc++.h>
using namespace __gnu_pbds;
typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> ost;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t, n; cin >> t;
    while (t--) {
        cin >> n; ost tree;
        long long sum = 0;
        for (int i = 1, x; i <= n; ++i) {
            cin >> x; tree.insert(x);
            auto it = tree.find_by_order(i / 2);
            sum += i % 2 ? *it : (*it + *--it) / 2;
        }
        cout << sum << '\n';
    }
    return 0;
}
