#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    for (char c; cin.get(c);) {
        int pos = keyboard.find(c);
        cout << (pos == -1 ? c : keyboard[pos - 1]);
    }
    return 0;
}
