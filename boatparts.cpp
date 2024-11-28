#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int p, n; cin >> p >> n;
    unordered_set<string> s;
    for (int i = 1; i <= n; ++i) {
        string w; cin >> w;
        if (s.insert(w).second && --p == 0) {
            cout << i << '\n';
            return 0;
        }
    }
    cout << "paradox avoided\n";
}
