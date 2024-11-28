#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    vector<int> a(n), b(n), seen(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int i = 0; i < n; ++i) cin >> b[a[i] - 1];
    int swaps = n;
    for (int i = 0; i < n; ++i) if (!seen[i]) {
        --swaps;
        for (int j = i; !seen[j]; j = b[j] - 1)
            seen[j] = 1;
    }
    cout << (swaps & 1 ? "Impossible\n" : "Possible\n");
    return 0;
}
