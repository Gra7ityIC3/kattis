#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string op, name;
    for (int i = 1, time; cin >> op; ++i) {
        map<string, int> mp;
        printf("Day %d\n", i);
        while (cin >> op, op != "CLOSE") {
            cin >> name >> time;
            mp[name] += op == "ENTER" ? -time : time;
        }
        for (const auto& [name, time] : mp)
            printf("%s $%.2f\n", name.c_str(), time * 0.1);
        printf("\n");
    }
    return 0;
}
