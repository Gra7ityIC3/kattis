#include <bits/stdc++.h>
using namespace std;

string solve(int n) {
    int p = 20, q = 1, s = 0;
    for (int i = 0, y; i < n; ++i) {
        cin >> y; p += y; s += y;
        if (++q == 5 && s < 10) return "Nothing";
        if (s >= 10) q = 1, s = 0;
        if (p >= 100) return "Touchdown";
        if (p <= 0) return "Safety";
    }
    return "Nothing";
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    cout << solve(n) << endl; 
    return 0;
}
