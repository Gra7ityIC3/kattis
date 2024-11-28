#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, ans = 0; string s; cin >> n >> s;
    for (int i = 0; i < n; ++i) {
        int freq[27] = {};
        for (int j = i; j < n; ++j) {
            ++freq[s[j] - 'a'];
            if (unordered_set<int>(freq, freq + 27).size() == 2)
                ans = max(ans, j - i + 1);
        }
    }
    cout << ans << endl;
    return 0;
}
