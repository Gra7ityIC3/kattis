#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, a, b, d; cin >> n >> a;
    for (int i = 0; i < n - 1; ++i) {
        cin >> b, d = gcd(a, b);
        printf("%d/%d\n", a / d, b / d);
    }
    return 0;
}
