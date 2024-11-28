#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; string a, b;
    cin >> n >> m >> a >> b;
    a = b.substr(0, m-n) + a;
    for (int i = m-n-1; i >= 0; --i)
        a[i] = (b[i+n] - a[i+n] + 26) % 26 + 'a';
    cout << a << endl;
    return 0;
}
