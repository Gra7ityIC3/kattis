#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank, setSize;
public:
  UnionFind(int n) : p(n), rank(n), setSize(n, 1) {
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
  int n, ans = 0; cin >> n;
  UnionFind UF(500001);
  for (int i = 0; i < n; ++i) {
    int m, sum = 0; cin >> m;
    unordered_set<int> s;
    for (int j = 0, x; j < m; ++j) {
        cin >> x;
        if (s.insert(UF.findSet(x)).second) sum += UF.sizeOfSet(x);
    }
    if (sum == m) {
        for (auto it = s.begin(); next(it) != s.end(); ++it)
            UF.unionSet(*it, *next(it));
        ++ans;
    }
  }
  cout << ans << endl;
  return 0;
}
