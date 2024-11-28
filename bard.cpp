#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(), (x).end()

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, e, k, a[100]; cin >> n >> e;
    vector<unordered_set<int>> villagers(n + 1);
    while (e--) {
        cin >> k;
        for (int i = 0; i < k; ++i) cin >> a[i];
        if (find(a, a + k, 1) != a + k) {
            for (int i = 0; i < k; ++i)
                villagers[a[i]].insert(e);
        } else {
            unordered_set<int> s;
            for (int i = 0; i < k; ++i)
                s.insert(all(villagers[a[i]]));
            for (int i = 0; i < k; ++i)
                villagers[a[i]] = s;
        }
    }
    for (int i = 1; i <= n; ++i)
        if (villagers[i].size() == villagers[1].size())
            cout << i << '\n';
    return 0;
}
