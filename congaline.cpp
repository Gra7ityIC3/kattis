#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, q; cin >> n >> q;
    list<string> l;
    unordered_map<string, list<string>::iterator> mp;
    for (int i = 0; i < n; ++i) {
        string a, b; cin >> a >> b;
        mp[b] = l.insert(l.end(), a);
        mp[a] = l.insert(l.end(), b);
    }
    auto it = l.begin();
    for (char c; cin >> c;) {
        switch (c) {
            case 'F':
                --it;
                break;
            case 'B':
                ++it;
                break;
            case 'R':
                if (it == --l.end()) {
                    it = l.begin();
                } else {
                    mp[*mp[*it]] = l.insert(l.end(), *it);
                    it = l.erase(it);
                }
                break;
            case 'C':
                mp[*mp[*it]] = l.insert(next(mp[*it]), *it);
                if ((it = l.erase(it)) == l.end())
                    it = l.begin();
                break;
            case 'P':
                cout << *mp[*it] << '\n';
                break;
        }
    }
    cout << '\n';
    for (string& s : l) cout << s << '\n';
    return 0;
}
