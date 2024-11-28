#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        int i = 1, n = s.length();
        while (i < n && s[i-1] <= s[i]) ++i;
        while (i < n && s[i-1] >= s[i]) ++i;
        s.replace(i, n - i, n - i, s[i-1]);
        cout << s << '\n';
    }
    return 0;
}
