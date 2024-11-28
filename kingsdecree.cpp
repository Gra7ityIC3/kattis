#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 300000;

int w[MAX_N], l[MAX_N];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int c; cin >> c;
    while (c--) {
        int n, lo = 0, hi = 0; cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> w[i], hi = max(hi, w[i]);
        for (int i = 0; i < n; ++i)
            cin >> l[i];
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            long long give = 0, take = 0;
            for (int i = 0; i < n; ++i)
                if (w[i] <= mid) take += mid - w[i];
                else give += min(w[i] - mid, w[i] - l[i]);
            take <= give ? lo = mid + 1 : hi = mid - 1;
        }
        cout << lo - 1 << '\n';
    }
    return 0;
}
