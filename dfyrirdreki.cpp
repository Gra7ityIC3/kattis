#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int a, b, c; cin >> a >> b >> c;
    int D = b * b - 4 * a * c;
    cout << (D > 0 ? 2 : D == 0) << endl;
    return 0;
}
