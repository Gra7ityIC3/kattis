#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t; cin >> t;
    while (t--) {
        int n, count = 0; cin >> n;
        unordered_map<int, int> mp{{0, 1}};
        for (int i = 0, sum = 0, x; i < n; ++i) {
            cin >> x; sum += x;
            count += mp[sum - 47];
            ++mp[sum];
        }
        cout << count << '\n';
    }
    return 0;
}
