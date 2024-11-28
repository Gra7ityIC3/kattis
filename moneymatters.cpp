#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank, setSize;
public:
  UnionFind(int n) : p(n), rank(n), setSize(n) {
    for (int i = 0; i < n; ++i) p[i] = i, cin >> setSize[i];
  }

  int findSet(int i) { return p[i] == i ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  int sizeOfSet(int i) { return setSize[findSet(i)]; }

  void unionSet(int i, int j) {
    int x = findSet(i), y = findSet(j);
    if (x == y) return;
    if (rank[x] > rank[y]) swap(x, y);
    p[x] = y;
    if (rank[x] == rank[y]) ++rank[y];
    setSize[y] += setSize[x];
  }
};

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int n, m, x, y; cin >> n >> m;
  UnionFind UF(n);
  for (int i = 0; i < m; ++i)
    cin >> x >> y, UF.unionSet(x, y);
  for (int i = 0; i < n; ++i)
    if (UF.sizeOfSet(i))
      return cout << "IMPOSSIBLE\n", 0;
  return cout << "POSSIBLE\n", 0;
}
