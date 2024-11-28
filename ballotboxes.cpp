#include <bits/stdc++.h>
using namespace std;

int n, b, a[500000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    while (cin >> n >> b && n != -1) {
        int lo = 1, hi = 0;
        for (int i = 0; i < n; ++i)
            cin >> a[i], hi = max(hi, a[i]);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            int sum = 0;
            for (int i = 0; i < n && sum <= b; ++i)
                sum += (a[i] + mid - 1) / mid;
            sum <= b ? hi = mid : lo = mid + 1;
        }
        cout << hi << '\n';
    }
    return 0;
}
