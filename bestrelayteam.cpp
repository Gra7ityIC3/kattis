#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n, first = 0; cin >> n;
    vector<tuple<double, double, string>> runners(n);
    for (auto& [b, a, name] : runners)
        cin >> name >> a >> b;
    sort(runners.begin(), runners.end());
    double bestTime = 80.0;
    for (int i = 0; i < n; ++i) {
        double time = get<1>(runners[i]);
        for (int j = 0, k = 0; j < 3; ++j, ++k) {
            k += k == i;
            time += get<0>(runners[k]);
        }
        if (time < bestTime) {
            bestTime = time;
            first = i;
        }
    }
    cout << bestTime << '\n' << get<2>(runners[first]) << '\n';
    for (int j = 0, k = 0; j < 3; ++j, ++k) {
        k += k == first;
        cout << get<2>(runners[k]) << '\n';
    }
    return 0;
}
