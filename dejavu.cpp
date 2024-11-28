#include <bits/stdc++.h>
using namespace std;

int x[100000], y[100000];
int freqX[100001], freqY[100001];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> x[i] >> y[i];
        ++freqX[x[i]];
        ++freqY[y[i]];
    }
    long long ans = 0;
    for (int i = 0; i < n; ++i)
        ans += (freqX[x[i]] - 1LL) * (freqY[y[i]] - 1LL);
    cout << ans << endl;
    return 0;
}
