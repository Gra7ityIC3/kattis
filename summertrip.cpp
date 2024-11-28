#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s; cin >> s;
    int ans = 0;
    for (int i = 0, n = s.length(); i < n; ++i) {
        int seen[123] = {};
        for (int j = i + 1; j < n && s[i] != s[j]; ++j)
            if (!seen[s[j]]) seen[s[j]] = 1, ++ans;
    }
    cout << ans << endl;
    return 0;
}
