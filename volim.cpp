#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int k, n, t; char z; cin >> k >> n;
    for (int game = 0; game <= 210; game += t) {
        if (z == 'T') k = (k % 8) + 1;
        cin >> t >> z;
    }
    cout << k << endl;
    return 0;
}
