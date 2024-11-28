#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, s; cin >> n >> s;
    int cur = s, ans = 0;
    for (int i = 0, x; i < n; ++i) {
        cin >> x; x += cin.peek() == 'L' && cin.get();
        if (cur < x) cur = s, ++ans;
        cur -= x;
    }
    cout << ans << endl;
    return 0;
}
