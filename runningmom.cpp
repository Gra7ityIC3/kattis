#include <bits/stdc++.h>
using namespace std;

enum { UNVISITED, EXPLORED, VISITED };

unordered_map<string, vector<string>> AL;
unordered_map<string, int> dfs_num;

bool cycleCheck(const string& u) {
    dfs_num[u] = EXPLORED;
    for (const string& v : AL[u])
        if (dfs_num[v] == UNVISITED) {
            if (cycleCheck(v)) return true;
        } else if (dfs_num[v] == EXPLORED)
            return true;
    dfs_num[u] = VISITED;
    return false;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    for (int i = 0; i < n; ++i) {
        string o, d; cin >> o >> d;
        AL[o].push_back(d);
    }
    for (string city; cin >> city;)
        cout << city << (cycleCheck(city) ? " safe\n" : " trapped\n");
    return 0;
}
