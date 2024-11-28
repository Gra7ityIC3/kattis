#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, a[1001]; cin >> n;
    for (int i = 0; i < n; ++i) cin >> a[i];
    sort(a, a + n);
    for (int i = 0, j = 0; i < n; i = ++j) {
        while (a[j] + 1 == a[j + 1]) ++j;
        if (i == j) printf("%d ", a[i]);
        else printf("%d%c%d ", a[i], i + 1 == j ? ' ' : '-', a[j]);
    }
    return 0;
}
