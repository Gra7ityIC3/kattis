#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
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
  int n, m;
  while (cin >> n >> m && n) {
    vector<iii> EL(m);
    for (auto& [w, u, v] : EL)
        cin >> u >> v >> w;
    sort(EL.begin(), EL.end());
    int mst_cost = 0; vector<ii> mst;
    UnionFind UF(n);
    for (auto& [w, u, v] : EL) {
        if (UF.isSameSet(u, v)) continue;
        mst_cost += w;
        mst.emplace_back(min(u, v), max(u, v));
        UF.unionSet(u, v);
        if (UF.numDisjointSets() == 1) break;
    }
    if (UF.numDisjointSets() == 1) {
        sort(mst.begin(), mst.end());
        cout << mst_cost << '\n';
        for (auto& [x, y] : mst)
            cout << x << ' ' << y << '\n';
    } else cout << "Impossible\n";
  }
  return 0;
}
