#include <bits/stdc++.h>
using namespace std;

int n, k, lo, hi = 1e9, w[100000];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> k;
    for (int i = 0; i < n; ++i)
        cin >> w[i], lo = max(lo, w[i]);
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        int sum = 0, cnt = 1;
        for (int i = 0; i < n; ++i) {
            sum += w[i];
            if (sum > mid) ++cnt, sum = w[i];
        }
        cnt <= k ? hi = mid : lo = mid + 1;
    }
    cout << hi << endl;
    return 0;
}
