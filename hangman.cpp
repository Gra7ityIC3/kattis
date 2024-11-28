#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string a, b; cin >> a >> b;
    unordered_set<char> s{a.begin(), a.end()};
    for (int i = 0, j = 10; !s.empty(); ++i)
        if (s.count(b[i])) s.erase(b[i]);
        else if (!--j) return cout << "LOSE\n", 0;
    return cout << "WIN\n", 0;
}
