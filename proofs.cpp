#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    unordered_set<string> s;
    for (int i = 1; i <= n; ++i) {
        string a, c;
        while (cin >> a && a != "->")
            if (!s.count(a)) { cout << i << endl; return 0; }
        cin >> c; s.insert(c);
    }
    cout << "correct\n";
}
