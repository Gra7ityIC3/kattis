#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int k, a, b, parent[101] = {}; cin >> k;
    while (cin >> a && a != -1) {
        string s; getline(cin, s);
        stringstream ss(s);
        while (ss >> b) parent[b] = a;
    }
    for (; k; k = parent[k]) cout << k << ' ';
    return 0;
}
