#include <bits/stdc++.h>
using namespace std;

typedef pair<int, string> is;

bool cmp(const is& a, const is& b) {
    return a.first == b.first ? a.second < b.second : a.first > b.first;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    vector<is> s1(n), s2(n), s3(n);
    for (int i = 0; i < n; ++i) {
        string name; cin >> name;
        s1[i].second = s2[i].second = s3[i].second = name;
        cin >> s1[i].first >> s2[i].first >> s3[i].first;
    }
    sort(s1.begin(), s1.end(), cmp);
    sort(s2.begin(), s2.end(), cmp);
    sort(s3.begin(), s3.end(), cmp);
    unordered_set<string> selected;
    for (int i = 0, j = 0, k = 0; n >= 3; n -= 3) {
        string names[3];
        while (!selected.insert(names[0] = s1[i++].second).second);
        while (!selected.insert(names[1] = s2[j++].second).second);
        while (!selected.insert(names[2] = s3[k++].second).second);
        sort(names, names + 3);
        for (string& name : names) cout << name << ' ';
        cout << '\n';
    }
    return 0;
}
