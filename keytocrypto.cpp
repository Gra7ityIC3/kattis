#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string a, b; cin >> a >> b;
    for (int i = 0; i < a.length(); ++i)
        b += a[i] = (a[i] - b[i] + 26) % 26 + 65;
    cout << a << endl;
    return 0;
}
