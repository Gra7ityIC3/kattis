#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    double x1, y1, x2, y2, p;
    while (cin >> x1 >> y1 >> x2 >> y2 >> p)
        printf("%f\n", pow(pow(abs(x1 - x2), p) + pow(abs(y1 - y2), p), 1 / p));
    return 0;
}
