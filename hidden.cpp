#include <bits/stdc++.h>
using namespace std;

int i, freq[91];

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s1, s2; cin >> s1 >> s2;
    for (char c : s1) ++freq[c];
    for (char c : s2) if (freq[c]) {
        if (s1[i] != c) break;
        --freq[c]; ++i;
    }
    cout << (i == s1.length() ? "PASS\n" : "FAIL\n");
    return 0;
}
