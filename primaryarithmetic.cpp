#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int a, b, carry, carries;
    while (cin >> a >> b && a || b) {
        carry = carries = 0;
        for (int i = 0; i < 9; ++i) {
            carry = a % 10 + b % 10 + carry > 9;
            carries += carry;
            a /= 10;
            b /= 10;
        }
        if (carries == 0) cout << "No carry operation.\n";
        else if (carries == 1) cout << "1 carry operation.\n";
        else cout << carries << " carry operations.\n";
    }
    return 0;
}
