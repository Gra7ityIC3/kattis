#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int t, n, k; cin >> t;
    long long ans, steps;
    list<int>::iterator p, q;
    while (t--) {
        cin >> n; list<int> st;
        for (int i = 0, s; i < n; ++i)
            cin >> s, st.push_back(s);
        ans = 0;
        while (true) {
            for (p = ++st.begin(); p != st.end() && *p >= *prev(p); ++p);
            if (p == st.end()) break;
            steps = 1, k = 2;
            for (q = st.begin(); *q < *p; ++q)
                if (*q == *next(q)) ++k;
                else steps *= k, k = 2;
            ans += steps;
            st.insert(q, *p);
            st.erase(p);
        }
        cout << ans << '\n';
    }
    return 0;
}
