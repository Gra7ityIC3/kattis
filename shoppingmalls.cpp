#include <bits/stdc++.h>
using namespace std;

struct point { int x, y, z; };

const double INF = 1e9;
const int MAX_N = 200;

double D[MAX_N][MAX_N];
int p[MAX_N][MAX_N];

void printPath(int i, int j) {
    if (i != j) printPath(i, p[i][j]);
    cout << j << ' ';
}

double dist(const point& a, const point& b) {
    int dx = a.x - b.x;
    int dy = a.y - b.y;
    int dz = 5 * (a.z - b.z);
    return sqrt(dx * dx + dy * dy + dz * dz);
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, m, a, b, q; string type; cin >> n >> m;
    vector<point> points(n);
    for (int i = 0; i < n; ++i) {
        auto& [x, y, z] = points[i];
        cin >> z >> x >> y;
        for (int j = 0; j < n; ++j) {
            D[i][j] = INF;
            p[i][j] = i;
        }
        D[i][i] = 0;
    }
    for (int i = 0; i < m; ++i) {
        cin >> a >> b >> type;
        D[a][b] = D[b][a] = dist(points[a], points[b]);
        if (type == "lift") {
            D[a][b] = D[b][a] = 1;
        } else if (type == "escalator") {
            D[a][b] = 1;
            D[b][a] *= 3;
        }
    }
    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (D[i][k] + D[k][j] < D[i][j]) {
                    D[i][j] = D[i][k] + D[k][j];
                    p[i][j] = p[k][j];
                }
    cin >> q;
    while (q--) {
        cin >> a >> b;
        printPath(a, b); cout << '\n';
    }
    return 0;
}
