#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MOD = 1e9 + 7;

ll N, T, A, B, C, t[10000];
ll sum, cnt, ans;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> N >> T >> A >> B >> C >> t[0];
    for (int i = 1; i < N; ++i)
        t[i] = (A * t[i - 1] + B) % C + 1;
    sort(t, t + N);
    for (int i = 0; i < N; ++i) {
        sum += t[i];
        if (sum > T) break;
        ++cnt; ans += sum;
    }
    printf("%d %d\n", cnt, ans % MOD);
    return 0;
}
