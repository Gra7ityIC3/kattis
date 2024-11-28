#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int a, l, n, kwf, sum = 0;
    for (int i = 0, a, l; i < 5; ++i)
        cin >> a >> l, sum += a * l;
    cin >> n >> kwf;
    cout << sum / 5 * n / kwf << endl;
    return 0;
}
