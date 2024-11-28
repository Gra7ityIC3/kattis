#include <bits/stdc++.h>
using namespace std;

#include <bits/extc++.h>
using namespace __gnu_pbds;
typedef tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update> ost;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s; ost tree;
    while (cin >> s) {
        if (s == "#") {
            auto it = tree.find_by_order(tree.size() / 2);
            cout << *it << '\n';
            tree.erase(it);
        } else {
            tree.insert(stoi(s));
        }
    }
    return 0;
}
