#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    unordered_map<string, int> mp;
    for (int i = 0; i < n; ++i) {
        string s; cin >> s;
        cout << mp[s] << '\n';
        for (int j = 1; j <= s.length(); ++j)
            ++mp[s.substr(0, j)];
    }
    return 0;
}
