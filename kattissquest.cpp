#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, e, g, x; cin >> n;
    map<int, priority_queue<int>> quests;
    quests[100001].push(0);
    for (int i = 0; i < n; ++i) {
        string s; cin >> s;
        if (s == "add") {
            cin >> e >> g;
            quests[e].push(g);
        } else {
            cin >> x;
            long long ans = 0;
            while (x >= quests.begin()->first) {
                auto it = quests.lower_bound(x);
                if (it->first > x) --it;
                auto& [e, pq] = *it;
                ans += pq.top(); pq.pop();
                if (pq.empty()) quests.erase(it);
                x -= e;
            }
            cout << ans << '\n';
        }
    }
    return 0;
}
