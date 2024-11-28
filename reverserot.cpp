#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; string s, alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
    while (cin >> n >> s) {
        reverse(s.begin(), s.end());
        for (char& c : s) c = alphabet[(alphabet.find(c) + n) % 28];
        cout << s << '\n';
    }
    return 0;
}
