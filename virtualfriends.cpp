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
  int t, f; cin >> t;
  while (t--) {
    cin >> f; UnionFind UF(2 * f);
    unordered_map<string, int> mp;
    for (int i = 0; i < f; ++i) {
      string a, b; cin >> a >> b;
      int x = mp.try_emplace(a, mp.size()).first->second;
      int y = mp.try_emplace(b, mp.size()).first->second;
      UF.unionSet(x, y);
      cout << UF.sizeOfSet(x) << '\n';
    }
  }
  return 0;
}
