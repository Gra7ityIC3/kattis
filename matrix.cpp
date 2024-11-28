#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int a, b, c, d;
    for (int i = 1; cin >> a >> b >> c >> d; ++i) {
        int det = a * d - b * c;
        printf("Case %d:\n%d %d\n %d %d\n", i, d / det, -b / det, -c / det, a / det);
    }
    return 0;
}
