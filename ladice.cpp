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

  bool unionSet(int i, int j) {
    int x = findSet(i), y = findSet(j);
    if (x != y) {
      if (rank[x] > rank[y]) swap(x, y);
      p[x] = y;
      if (rank[x] == rank[y]) ++rank[y];
      setSize[y] += setSize[x];
      setSize[x] = 0;
    }
    return setSize[y] && setSize[y]--;
  }
};

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int n, l, a, b; cin >> n >> l;
  UnionFind UF(l);
  for (int i = 0; i < n; ++i) {
    cin >> a >> b;
    cout << (UF.unionSet(a, b) ? "LADICA\n" : "SMECE\n");
  }
  return 0;
}
