#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> iii;
typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank;
  int numSets;
public:
  UnionFind(int n) : p(n), rank(n), numSets(n) {
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
  vector<iii> EL(m);
  for (auto& [w, u, v] : EL)
      cin >> u >> v >> w;
  sort(EL.begin(), EL.end());
  UnionFind UF(n);
  for (auto& [w, u, v] : EL) {
      if (UF.isSameSet(u, v)) continue;
      UF.unionSet(u, v);
      if (UF.numDisjointSets() == 1) {
        cout << w << endl;
        return 0;
      }
  }
  cout << "IMPOSSIBLE\n";
}
