#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, ans = 0; cin >> n >> m;
    vector<int> start(n), end(n);
    for (int i = 0; i < n; ++i) {
        cin >> start[i] >> end[i];
        end[i] += start[i];
    }
    sort(start.begin(), start.end());
    sort(end.begin(), end.end());
    for (int i = 1, j = 0; i < n; ++i)
        while (start[i] >= end[j])
            if (start[i] <= end[j++] + m) {
                ++ans; break;
            }
    cout << ans << endl;
    return 0;
}
