#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, sum = 0; cin >> n;
    vector<int> d(n);
    for (int i = 0; i < n; ++i)
        cin >> d[i], sum += d[i];
    set<int> ans;
    for (int i = 0; i < n; ++i)
        ans.insert(sum - d[i]);
    cout << ans.size() << '\n';
    for (int D : ans) cout << D << ' ';
    return 0;
}
