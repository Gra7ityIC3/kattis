#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, c[10001]; cin >> n;
    iota(c, c + 10001, 0);
    unordered_set<int> s;
    for (int i = 0, x, y; i < n; ++i) {
        cin >> x;
        for (y = c[x]; !s.insert(y).second; y += x);
        c[x] = y;
        cout << y << '\n';
    }
    return 0;
}
