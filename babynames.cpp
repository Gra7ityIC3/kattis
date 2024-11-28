#include <bits/stdc++.h>
using namespace std;

#include <bits/extc++.h>
using namespace __gnu_pbds;
typedef tree<string, null_type, less<string>, rb_tree_tag, tree_order_statistics_node_update> ost;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    ost male, female;
    int cmd;
    while (cin >> cmd && cmd) {
        string babyName, start, end;
        int genderSuitability, ans = 0;
        if (cmd == 1) {
            cin >> babyName >> genderSuitability;
            (genderSuitability == 1 ? male : female).insert(babyName);
        } else if (cmd == 2) {
            cin >> babyName;
            if (!male.erase(babyName)) female.erase(babyName);
        } else {
            cin >> start >> end >> genderSuitability;
            if (genderSuitability == 0 || genderSuitability == 1) {
                ans += male.order_of_key(end) - male.order_of_key(start);
            }
            if (genderSuitability == 0 || genderSuitability == 2) {
                ans += female.order_of_key(end) - female.order_of_key(start);
            }
            cout << ans << '\n';
        }
    }
    return 0;
}
