#include <bits/stdc++.h>
using namespace std;

int n, b, a[100000];
int pos, ans;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> b;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        if (a[i] == b) pos = i;
    }
    unordered_map<int, int> mp;
    for (int i = pos, delta = 0; i >= 0; --i) {
        if (a[i] > b) ++delta;
        else if (a[i] < b) --delta;
        ++mp[delta];
    }
    for (int i = pos, delta = 0; i < n; ++i) {
        if (a[i] > b) ++delta;
        else if (a[i] < b) --delta;
        ans += mp[-delta];
    }
    cout << ans << endl;
    return 0;
}
