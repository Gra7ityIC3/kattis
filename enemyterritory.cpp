#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int N, X, Y, xi, yi, xr, yr, x, y;
    cin >> N >> X >> Y >> xi >> yi >> xr >> yr;
    vector<vi> dist(X, vi(Y, -1));
    queue<ii> q;
    for (int i = 0; i < N; ++i) {
        cin >> x >> y;
        dist[x][y] = 0;
        q.emplace(x, y);
    }
    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();
        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            if (nx < 0 || nx >= X || y < 0 || y >= Y) continue;
            if (dist[nx][ny] != -1) continue;
            dist[nx][ny] = dist[x][y] + 1;
            q.emplace(nx, ny);
        }
    }
    int lo = -1, hi = min(dist[xi][yi], dist[xr][yr]), ans;
    while (lo != hi) {
        int mid = (lo + hi + 1) / 2;
        vector<vi> dist2(X, vi(Y, -1));
        dist2[xi][yi] = 0;
        q.emplace(xi, yi);
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (int d = 0; d < 4; ++d) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx < 0 || nx >= X || y < 0 || y >= Y) continue;
                if (dist[nx][ny] < mid) continue;
                if (dist2[nx][ny] != -1) continue;
                dist2[nx][ny] = dist2[x][y] + 1;
                q.emplace(nx, ny);
            }
        }
        if (dist2[xr][yr] == -1) hi = mid - 1;
        else lo = mid, ans = dist2[xr][yr];
    }
    printf("%d %d\n", lo, ans);
    return 0;
}
