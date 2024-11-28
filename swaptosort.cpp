#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank;
public:
  UnionFind(int n) : p(n + 1), rank(n + 1) {
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
  int n, k, a, b; cin >> n >> k;
  UnionFind UF(n);
  for (int i = 0; i < k; ++i)
    cin >> a >> b, UF.unionSet(a, b);
  for (int i = 1; i <= n / 2; ++i)
    if (!UF.isSameSet(i, n - i + 1))
      return cout << "No\n", 0;
  return cout << "Yes\n", 0;
}
