#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, c; cin >> n;
    list<string> q; string op, a, b;
    for (int i = 0; i < n; ++i)
        cin >> a, q.push_back(a);
    cin >> c;
    for (int i = 0; i < c; ++i) {
        cin >> op >> a;
        if (op == "cut") {
            cin >> b;
            q.insert(find(q.begin(), q.end(), b), a);
        } else {
            q.erase(find(q.begin(), q.end(), a));
        }
    }
    for (string& a : q) cout << a << '\n';
    return 0;
}
