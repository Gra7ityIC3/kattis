#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s; cin >> s;
    int n = s.length() / 2;
    string left = s.substr(0, n);
    string right = s.substr(n, n);
    int r1 = 0, r2 = 0;
    for (int i = 0; i < n; ++i)
        r1 += left[i], r2 += right[i];
    for (int i = 0; i < n; ++i)
        left[i] = (left[i] + right[i] + r1 + r2) % 26 + 65;
    cout << left << endl;
    return 0;
}
