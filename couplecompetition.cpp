#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m = 0; cin >> n;
    vector<int> h(n), dist(n, -1);
    vector<vector<int>> AL(n);
    stack<int> st; queue<int> q;

    for (int i = 0; i < n; ++i)
        cin >> h[i], m = max(m, h[i]);

    for (int i = 0; i < n; ++i) {
        if (h[i] == m) dist[i] = 0, q.push(i);
        while (!st.empty() && h[st.top()] <= h[i]) st.pop();
        if (!st.empty()) AL[st.top()].push_back(i);
        st.push(i);
    }

    for (int i = n - 1; i >= 0; --i) {
        while (!st.empty() && h[st.top()] <= h[i]) st.pop();
        if (!st.empty()) AL[st.top()].push_back(i);
        st.push(i);
    }

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : AL[u])
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
    }

    for (int v = 0; v < n; ++v)
        cout << dist[v] << ' ';
    return 0;
}
