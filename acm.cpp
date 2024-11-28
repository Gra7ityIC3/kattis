#include <bits/stdc++.h>
using namespace std;

int m, cnt, ans, wa[91];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    while (cin >> m && m != -1) {
        char c; string s; cin >> c >> s;
        s == "right" ?  ++cnt, ans += m + 20 * wa[c] : ++wa[c];
    }
    printf("%d %d\n", cnt, ans);
    return 0;
}
