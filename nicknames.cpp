#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int a, b; cin >> a;
    unordered_map<string, int> freq;
    for (int i = 0; i < a; ++i) {
        string n; cin >> n;
        for (int j = 1; j <= n.length(); ++j)
            ++freq[n.substr(0, j)];
    }
    cin >> b;
    for (int i = 0; i < b; ++i) {
        string k; cin >> k;
        cout << freq[k] << '\n';
    }
    return 0;
}
