#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, guess, q, idea; string name; cin >> n;
    map<int, string> game{{-1, ":("}};
    for (int i = 0; i < n; ++i) {
        cin >> name >> guess;
        game[guess] = name;
    }
    cin >> q;
    while (q--) {
        cin >> idea;
        auto it = game.lower_bound(idea);
        if (it == game.end() || it->first != idea)
            cout << (--it)->second << '\n';
        else
            cout << it->second << '\n';
    }
    return 0;
}
