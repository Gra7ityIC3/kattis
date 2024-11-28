#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s; cin >> s;
    for (int i = 0, n = s.length(); i < n; ++i) {
        if (i < n - 2 && s[i] + s[i+1] + s[i+2] == 'R' + 'B' + 'L') {
            cout << 'C';
            i += 2;
        } else if (s[i] == 'R') {
            cout << 'S';
        } else if (s[i] == 'B') {
            cout << 'K';
        } else {
            cout << 'H';
        }
    }
    return 0;
}
