#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, k = 0; cin >> n;
    vector<int> A(n + 1), L(n + 1);
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        A[x] = i;
    }
    for (int i = 0; i < n; ++i) {
        int x; cin >> x;
        int pos = lower_bound(L.begin(), L.begin() + k, A[x]) - L.begin();
        L[pos] = A[x];
        if (pos == k) ++k;
    }
    printf("2 %d\n", k + 1);
    return 0;
}
