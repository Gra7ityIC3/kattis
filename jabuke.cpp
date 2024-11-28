#include <bits/stdc++.h>
using namespace std;

struct point { int x, y; };

int area(point A, point B, point C) {
    return abs(A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y));
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    point A, B, C, P; int n, ans = 0;
    cin >> A.x >> A.y >> B.x >> B.y >> C.x >> C.y >> n;
    while (n--) {
        cin >> P.x >> P.y;
        ans += area(A, B, P) + area(A, C, P) + area(B, C, P) == area(A, B, C);
    }
    printf("%.1lf\n%d\n", area(A, B, C) / 2.0, ans);
    return 0;
}
