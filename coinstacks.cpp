#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    vector<pair<int, int>> stacks(n), moves;
    for (int i = 0; i < n; ++i) {
        cin >> stacks[i].first;
        stacks[i].second = i + 1;
    }
    while (sort(stacks.rbegin(), stacks.rend()), stacks[1].first) {
        moves.emplace_back(stacks[0].second, stacks[1].second);
        --stacks[0].first;
        --stacks[1].first;
    }
    if (stacks[0].first) {
        cout << "no\n";
    } else {
        cout << "yes\n";
        for (auto& [a, b] : moves)
            cout << a << ' ' << b << '\n';
    }
    return 0;
}
