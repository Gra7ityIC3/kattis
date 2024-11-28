#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    list<char> l; auto it = l.begin();
    string s; cin >> s;
    for (char c : s) {
        if (c == 'L') --it;
        else if (c == 'R') ++it;
        else if (c == 'B') it = l.erase(--it);
        else l.insert(it, c);
    }
    for (char c : l) cout << c;
    return 0;
}
