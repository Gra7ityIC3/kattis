#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a[100000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int m, n; cin >> m >> n;
    ll sum = -m, ans = 0;
    for (int i = 0; i < n; ++i)
        cin >> a[i], sum += a[i];
    sort(a, a + n);
    for (int i = 0; i < n; ++i) {
        ll w = min(a[i], sum / (n - i));
        ans += w * w;
        sum -= w;
    }
    cout << ans << endl;
    return 0;
}
