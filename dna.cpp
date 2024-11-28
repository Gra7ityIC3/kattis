#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, ans = 0; string s; cin >> n >> s;
    bool flip = false;
    for (int i = n - 1; i >= 0; --i)
        if (s[i] == 'B' != flip)
            ++ans, flip = s[i - 1] == 'B';
    cout << ans << endl;
    return 0;
}
