#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank;
  int numSets;
public:
  UnionFind(int n) : p(n + 1), rank(n + 1), numSets(n) {
    iota(p.begin(), p.end(), 0);
  }

  int findSet(int i) { return p[i] == i ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  int numDisjointSets() { return numSets; }

  void unionSet(int i, int j) {
    int x = findSet(i), y = findSet(j);
    if (x == y) return;
    if (rank[x] > rank[y]) swap(x, y);
    p[x] = y;
    if (rank[x] == rank[y]) ++rank[y];
    --numSets;
  }
};

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int n, m; cin >> n >> m;
  UnionFind UF(n);
  for (int i = 0, a, b; i < m; ++i)
    cin >> a >> b, UF.unionSet(a, b);
  if (UF.numDisjointSets() == 1) {
    cout << "Connected\n";
  } else {
    for (int i = 2; i <= n; ++i)
      if (!UF.isSameSet(i, 1))
        cout << i << '\n';
  }
  return 0;
}
