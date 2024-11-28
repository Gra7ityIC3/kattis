#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    vector<bool> used(n + 1);
    vector<int> gnomes(m);
    for (int& g : gnomes)
        cin >> g, used[g] = true;
    int i = 1;
    for (int g : gnomes) {
        for (; i < g; ++i) if (!used[i])
            cout << i << '\n';
        cout << g << '\n';
    }
    for (; i <= n; ++i) if (!used[i])
        cout << i << '\n';
    return 0;
}
