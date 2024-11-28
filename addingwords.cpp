#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    unordered_map<string, int> m1;
    unordered_map<int, string> m2;
    string cmd;
    while (cin >> cmd) {
        if (cmd == "def") {
            string x; int y; cin >> x >> y;
            if (m1.count(x)) m2.erase(m1[x]);
            m1[x] = y;
            m2[y] = x;
        } else if (cmd == "calc") {
            string x; char op = '+';
            int res = 0;
            bool valid = true;
            while (op != '=') {
                cin >> x;
                if (m1.count(x)) res += op == '+' ? m1[x] : -m1[x];
                else valid = false;
                cin >> op;
                cout << x << ' ' << op << ' ';
            }
            cout << (valid && m2.count(res) ? m2[res] : "unknown") << '\n';
        } else {
            m1.clear();
            m2.clear();
        }
    }
    return 0;
}
