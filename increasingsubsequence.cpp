#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 200;

int A[MAX_N], L[MAX_N], L_id[MAX_N], p[MAX_N];

void print_LIS(int i) {
    if (p[i] == -1) { cout << A[i]; return; }
    print_LIS(p[i]);
    cout << ' ' << A[i];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n;
    while (cin >> n && n) {
        for (int i = 0; i < n; ++i)
            cin >> A[i], p[i] = -1;
        int k = 0, lis_end = 0;
        for (int i = 0; i < n; ++i) {
            int pos = lower_bound(L, L+k, A[i]) - L;
            L[pos] = A[i];
            L_id[pos] = i;
            p[i] = pos ? L_id[pos-1] : -1;
            if (pos >= k - 1) {
                lis_end = i;
                if (pos == k) ++k;
            }
        }
        cout << k << ' ';
        print_LIS(lis_end); cout << '\n';
    }
    return 0;
}
