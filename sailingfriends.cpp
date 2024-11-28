#include <bits/stdc++.h>
using namespace std;

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
  int N, B, M, a, b; cin >> N >> B >> M;
  vector<int> ids(B);
  for (int& id : ids) cin >> id;
  UnionFind UF(N);
  for (int i = 0; i < M; ++i)
    cin >> a >> b, UF.unionSet(a, b);
  unordered_set<int> s;
  for (int i = 1; i <= N; ++i)
    s.insert(UF.findSet(i));
  int ans = UF.numDisjointSets();
  for (int id : ids)
    ans -= s.erase(UF.findSet(id));
  cout << ans << endl;
  return 0;
}
