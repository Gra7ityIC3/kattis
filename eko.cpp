#include <bits/stdc++.h>
using namespace std;

int n, m, lo, hi, a[1000000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> a[i], hi = max(hi, a[i]);
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        long long sum = 0;
        for (int i = 0; i < n; ++i)
            sum += max(0, a[i] - mid);
        sum >= m ? lo = mid : hi = mid - 1;
    }
    cout << lo << endl;
    return 0;
}
