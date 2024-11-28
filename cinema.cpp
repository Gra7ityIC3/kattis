#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, x, sum = 0; cin >> n >> m;
    while (cin >> x)
        if (sum + x <= n) sum += x, --m;
    cout << m << endl;
    return 0;
}
