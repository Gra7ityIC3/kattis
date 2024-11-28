#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank;
public:
  UnionFind(int n) : p(n), rank(n) {
    iota(p.begin(), p.end(), 0);
  }

  int findSet(int i) { return p[i] == i ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  void unionSet(int i, int j) {
    int x = findSet(i), y = findSet(j);
    if (x == y) return;
    if (rank[x] > rank[y]) swap(x, y);
    p[x] = y;
    if (rank[x] == rank[y]) ++rank[y];
  }
};

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int n, q, a, b; cin >> n >> q;
  UnionFind UF(n);
  while (q--) {
    char op; cin >> op >> a >> b;
    if (op == '=') UF.unionSet(a, b);
    else cout << (UF.isSameSet(a, b) ? "yes\n" : "no\n");
  }
  return 0;
}
