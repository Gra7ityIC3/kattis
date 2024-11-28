#include <bits/stdc++.h>
using namespace std;

const int MAX_TIME = 86400;

int freq[MAX_TIME];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, l, r; cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> m;
        for (int j = 0; j < m; ++j) {
            cin >> l >> r;
            for (int k = l; k <= r; ++k) ++freq[k];
        }
    }
    int ans = *max_element(freq, freq + MAX_TIME);
    int cnt = count(freq, freq + MAX_TIME, ans);
    printf("%d\n%d\n", ans, cnt);
    return 0;
}
