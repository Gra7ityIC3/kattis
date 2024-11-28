#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, a = 1, b; cin >> n;
    vector<list<string>> S(n + 1);
    for (int i = 1; i <= n; ++i) {
        string s; cin >> s;
        S[i].push_back(s);
    }
    for (int i = 1; i < n; ++i) {
        cin >> a >> b;
        S[a].splice(S[a].end(), S[b]);
    }
    for (string& s : S[a]) cout << s;
    return 0;
}
