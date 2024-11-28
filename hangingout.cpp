#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int L, x; cin >> L >> x;
    int count = 0, ans = 0;
    for (int i = 0; i < x; ++i) {
        string ev; int p; cin >> ev >> p;
        if (ev == "enter")
            if (count + p > L) ++ans;
            else count += p;
        else
            count -= p;
    }
    cout << ans << endl;
    return 0;
}
