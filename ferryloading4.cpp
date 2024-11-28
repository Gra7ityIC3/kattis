#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int c, fl, m, lc, rc, cll, crl, l;
    cin >> c;
    while (c--) {
        cin >> fl >> m;
        fl *= 100;
        lc = rc = cll = crl = 0;
        while (m--) {
            string s; cin >> l >> s;
            if (s == "left")
                cll + l > fl ? ++lc, cll = l : cll += l;
            else
                crl + l > fl ? ++rc, crl = l : crl += l;
        }
        lc += cll > 0;
        rc += crl > 0;
        cout << (lc <= rc ? 2 * rc : 2 * lc - 1) << '\n';
    }
    return 0;
}
