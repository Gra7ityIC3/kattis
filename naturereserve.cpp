#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> iii;
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
  int t, n, m, l, s, u, v; cin >> t;
  while (t--) {
    cin >> n >> m >> l >> s >> u;
    UnionFind UF(n);
    for (int i = 1; i < s; ++i) {
      cin >> v; UF.unionSet(u, v); u = v;
    }
    vector<iii> EL(m);
    for (auto& [w, u, v] : EL)
      cin >> u >> v >> w;
    sort(EL.begin(), EL.end());
    long long ans = 0;
    for (auto& [w, u, v] : EL) {
      if (UF.isSameSet(u, v)) continue;
      ans += w;
      UF.unionSet(u, v);
      if (UF.numDisjointSets() == 1) break;
    }
    cout << ans + 1LL * (n - s) * l << '\n';
  }
  return 0;
}
