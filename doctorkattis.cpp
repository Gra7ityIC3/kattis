#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, string> iis;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    set<iis> s;
    unordered_map<string, iis> mp;
    for (int i = n - 1; i >= 0; --i) {
        int op, infectionLevel, increaseInfection; string catName; cin >> op;
        if (op == 0) {
            cin >> catName >> infectionLevel;
            s.insert(mp[catName] = {infectionLevel, i, catName});
        } else if (op == 1) {
            cin >> catName >> increaseInfection;
            iis cat = mp[catName];
            s.erase(cat);
            get<0>(cat) += increaseInfection;
            s.insert(mp[catName] = cat);
        } else if (op == 2) {
            cin >> catName;
            s.erase(mp[catName]);
        } else {
            cout << (s.empty() ? "The clinic is empty" : get<2>(*s.rbegin())) << '\n';
        }
    }
    return 0;
}
