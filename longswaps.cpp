#include <bits/stdc++.h>
using namespace std;

string s; int k;

string solve(string t, int n) {
    sort(t.begin(), t.end());
    for (int i = n - k; i < k; ++i)
        if (t[i] != s[i]) return "No";
    return "Yes";
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> s >> k;
    cout << solve(s, s.length()) << endl;
    return 0;
}
