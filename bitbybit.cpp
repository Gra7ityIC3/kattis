#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n;
    while (cin >> n && n) {
        string s(32, '?');
        while (n--) {
            string op; int i, j;
            cin >> op >> i;
            if (op == "CLEAR") {
                s[i] = '0';
            } else if (op == "SET") {
                s[i] = '1';
            } else if (op == "OR") {
                cin >> j;
                s[i] = s[i] == '1' || s[j] == '1' ? '1' : s[i] == '0' && s[j] == '0' ? '0' : '?';
            } else {
                cin >> j;
                s[i] = s[i] == '1' && s[j] == '1' ? '1' : s[i] == '0' || s[j] == '0' ? '0' : '?';
            }
        }
        reverse(s.begin(), s.end());
        cout << s << '\n';
    }
    return 0;
}
