#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t; cin >> ws;
    while (t--) {
        list<char> l; auto it = l.begin();
        string s; getline(cin, s);
        for (char c : s) {
            if (c == '<') {
                if (it != l.begin())
                    it = l.erase(--it);
            } else if (c == '[') {
                it = l.begin();
            } else if (c == ']') {
                it = l.end();
            } else {
                l.insert(it, c);
            }
        }
        for (char c : l) cout << c;
        cout << '\n';
    }
    return 0;
}
