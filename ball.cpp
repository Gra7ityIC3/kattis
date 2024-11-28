#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, a, b; cin >> n;
    vector<int> cnt(n + 1);
    for (int i = n / 2; i <= n; ++i) {
        cin >> a >> b;
        ++cnt[a]; ++cnt[b];
    }
    for (int i = 1; i <= n; ++i)
        if (cnt[i] > 1) cout << i << ' ';
    return 0;
}
