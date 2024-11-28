#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 200010;

string T, P;
int b[MAX_N], n, m;

void kmpPreprocess() {
    int i = 0, j = -1; b[0] = -1;
    while (i < m) {
        while (j >= 0 && P[i] != P[j]) j = b[j];
        b[++i] = ++j;
    }
}

void kmpSearch() {
    int i = 0, j = 0;
    while (i < n) {
        while (j >= 0 && T[i] != P[j]) j = b[j];
        ++i; ++j;
        if (j == m) {
            cout << i - j << ' ';
            j = b[j];
        }
    }
    cout << '\n';
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    while (getline(cin, P) && getline(cin, T)) {
        n = T.length();
        m = P.length();
        kmpPreprocess();
        kmpSearch();
    }
    return 0;
}
