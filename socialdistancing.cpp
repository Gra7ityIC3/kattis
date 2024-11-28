#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, x; cin >> n >> x;
    priority_queue<int> pq;
    for (int i = 1; i < n; ++i) {
        cin >> x; pq.push(x); pq.push(x); pq.pop();
    }
    long long ans = 0;
    while (!pq.empty()) {
        ans += pq.top(); pq.pop();
    }
    cout << ans << endl;
    return 0;
}
