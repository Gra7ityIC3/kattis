#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int W, N; cin >> W >> N;
    long long A = 0;
    for (int i = 0, w, l; i < N; ++i)
        cin >> w >> l, A += w * l;
    cout << A / W << endl;
    return 0;
}
