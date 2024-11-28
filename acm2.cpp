#include <bits/stdc++.h>
using namespace std;

int n, p, a[13];
int sum, cnt, ans;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> p;
    for (int i = 0; i < n; ++i) cin >> a[i];
    swap(a[0], a[p]);
    sort(a + 1, a + n);
    for (int i = 0; i < n; ++i) {
        sum += a[i];
        if (sum > 300) break;
        ++cnt; ans += sum;
    }
    printf("%d %d\n", cnt, ans);
    return 0;
}
