#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k; cin >> n >> k;
    unordered_map<int, int> mp;
    for (int i = 0, x; i < n; ++i)
        cin >> x, ++mp[x];
    priority_queue<int> pq;
    for (const auto& [k, v] : mp)
        pq.push(v);
    for (int i = 0; i < k; ++i)
        pq.push(pq.top() - 1), pq.pop();
    cout << pq.top() << endl;
    return 0;
}
