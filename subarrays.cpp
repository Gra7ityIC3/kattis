#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    ll n, k, b, sum = 0; cin >> n >> k >> b;
    unordered_map<ll, int> mp{{0, -1}};
    for (int i = 0, x; i < n; ++i) {
        cin >> x; sum += x;
        ll beauty = sum - (i + 1) * k;
        if (mp.count(beauty - b)) {
            printf("%d %d\n", mp[beauty - b] + 1, i);
            return 0;
        }
        mp.try_emplace(beauty, i);
    }
    printf("-1\n");
}
