#include <bits/stdc++.h>
using namespace std;

#define LSOne(S) ((S) & -(S))

typedef vector<int> vi;

class FenwickTree {
private:
  vi ft;
public:
  FenwickTree(int m) : ft(m + 1) {}

  int rsq(int j) {
    int sum = 0;
    for (; j; j -= LSOne(j))
      sum += ft[j];
    return sum;
  }

  int rsq(int i, int j) { return rsq(j) - rsq(i - 1); }

  void update(int i, int v) {
    for (; i < ft.size(); i += LSOne(i))
      ft[i] += v;
  }
};

int main() {
  cin.tie(0)->sync_with_stdio(0);
  int n, k, l, r; cin >> n >> k;
  FenwickTree ft(n);
  while (k--) {
    char op; cin >> op >> l;
    if (op == 'F')
      ft.update(l, !ft.rsq(l, l) ? 1 : -1);
    else {
      cin >> r;
      cout << ft.rsq(l, r) << '\n';
    }
  }
  return 0;
}
