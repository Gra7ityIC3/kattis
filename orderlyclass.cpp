#include <bits/stdc++.h>
using namespace std;

int solve(string& a, string& b, int n) {
    int l = 0, r = n - 1, ans = 1;
    while (l < n && a[l] == b[l]) ++l;
    while (r >= 0 && a[r] == b[r]) --r;
    for (int i = 0; i < r - l + 1; ++i)
        if (a[l + i] != b[r - i]) return 0;
    while (--l >= 0 && ++r < n && a[l] == a[r]) ++ans;
    return ans;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string a, b; cin >> a >> b;
    cout << solve(a, b, a.length()) << endl;
    return 0;
}
