#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    string s; cin >> s;
    for (int i = 0, indent = 0; i < s.length(); ++i) {
        switch (s[i]) {
            case '{':
                printf("{\n");
                if (s[i + 1] == '}') {
                    printf("%*s}", indent, "");
                    ++i;
                } else {
                    printf("%*s", indent += 2, "");
                }
                break;
            case '}':
                if (s[i - 1] != '{')
                    printf("\n%*s}", indent -= 2, "");
                break;
            case ',':
                printf(",\n%*s", indent, "");
                break;
            default:
                printf("%c", s[i]);
                break;
        }
    }
    printf("\n");
    return 0;
}
