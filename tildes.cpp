#include <bits/stdc++.h>
using namespace std;

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
  int n, q, a, b; cin >> n >> q;
  UnionFind UF(n);
  while (q--) {
    char op; cin >> op >> a;
    if (op == 't') cin >> b, UF.unionSet(a, b);
    else cout << UF.sizeOfSet(a) << '\n';
  }
  return 0;
}
