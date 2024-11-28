#include <bits/stdc++.h>
using namespace std;

int n, a[1000000];
long long sum, ans;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n;
    for (int i = 0, j = 2; i < n; ++i) {
        cin >> a[i];
        sum += j * a[i];
        if (a[i]) ++j;
    }
    ans = sum;
    for (int i = 0; i < n; ++i)
        ans = max(ans, sum -= a[i]);
    cout << ans << endl;
    return 0;
}
