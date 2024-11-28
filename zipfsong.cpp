#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m; cin >> n >> m;
    priority_queue<tuple<long long, int, string>> pq;
    for (int i = 1; i <= n; ++i) {
        long long f; string s; cin >> f >> s;
        pq.push({f * i, -i, s});
    }
    for (int i = 0; i < m; ++i) {
        cout << get<2>(pq.top()) << '\n'; pq.pop();
    }
    return 0;
}
