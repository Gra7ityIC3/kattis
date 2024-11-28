#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int s, c, k, ans = 1; cin >> s >> c >> k;
    vector<int> d(s);
    for (int i = 0; i < s; ++i) cin >> d[i];
    sort(d.begin(), d.end());
    for (int i = 1, j = 0, cnt = 1; i < s; ++i)
        d[i] - d[j] > k || cnt == c ? ++ans, cnt = 1, j = i : ++cnt;
    cout << ans << endl;
    return 0;
}
