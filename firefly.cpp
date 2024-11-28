#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, h, cnt, ans = 1e9; cin >> n >> h;
    vector<int> stalagmites(h + 1), stalactites(h + 1);
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        i % 2 ? ++stalactites[x] : ++stalagmites[x];
    }
    for (int i = h - 2; i > 0; --i) {
        stalagmites[i] += stalagmites[i + 1];
        stalactites[i] += stalactites[i + 1];
    }
    for (int i = 1; i <= h; ++i) {
        int sum = stalagmites[i] + stalactites[h - i + 1];
        if (sum < ans) ans = sum, cnt = 1;
        else if (sum == ans) ++cnt;
    }
    printf("%d %d\n", ans, cnt);
    return 0;
}
