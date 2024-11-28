#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, k, p; cin >> n >> m;
    unordered_set<int> s;
    for (int i = 0; i < n; ++i) {
        cin >> k;
        for (int j = 0; j < k; ++j)
            cin >> p, s.insert(p);
    }
    cout << (s.size() == m ? "Jebb\n" : "Neibb\n");
    return 0;
}
