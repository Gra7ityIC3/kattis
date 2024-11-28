#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int h, x = 1; cin >> h;
    for (char c; cin >> c;)
        x = x * 2 + (c == 'R');
    cout << (1 << h + 1) - x << endl;
    return 0;
}
