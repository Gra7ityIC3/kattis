#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, r1, c1, r2, c2;
    setlinebuf(stdout);
    scanf("%d", &t);
    while (t--) {
        printf("3 1 3 6\n");
        while (scanf("\nMOVE %d %d %d %d", &r1, &c1, &r2, &c2) == 4)
            printf("%d %d %d %d\n", 6 - r2, 7 - c2, 6 - r1, 7 - c1);
        scanf("GAME");
    }
    return 0;
}
