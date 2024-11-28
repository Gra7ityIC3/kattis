#include <bits/stdc++.h>
using namespace std;

typedef tuple<int, int, int> iii;
typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank, setSize;
public:
  UnionFind(int n) : p(n + 1), rank(n + 1), setSize(n + 1, 1) {
    iota(p.begin(), p.end(), 0);
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
  int t, n; cin >> t;
  while (t--) {
    cin >> n;
    vector<iii> EL(n - 1);
    for (auto& [w, u, v] : EL)
      cin >> u >> v >> w;
    sort(EL.begin(), EL.end());
    long long ans = 0;
    UnionFind UF(n);
    for (auto& [w, u, v] : EL) {
      ans += w + (w + 1LL) * (UF.sizeOfSet(u) * UF.sizeOfSet(v) - 1);
      UF.unionSet(u, v);
    }
    cout << ans << '\n';
  }
  return 0;
}
