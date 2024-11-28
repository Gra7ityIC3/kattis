#include <bits/stdc++.h>
using namespace std;

int N, x, y, L[100000];
int sum, ans;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> x >> y;
    for (int i = 0; i < N; ++i) cin >> L[i];
    sort(L, L + N);
    for (int i = 0; i < N; ++i) {
        sum += L[i] * x;
        if (sum > y * (i + 1)) break;
        ++ans;
    }
    cout << ans << endl;
    return 0;
}
