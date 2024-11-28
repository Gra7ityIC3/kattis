#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);
    int n; cin >> n;
    deque<int> front, back;
    for (int i = 0, x; i < n; ++i) {
        string s; cin >> s >> x;
        if (s == "push_back")
            back.push_back(x);
        else if (s == "push_front")
            front.push_front(x);
        else if (s == "push_middle")
            front.push_back(x);
        else {
            cout << (x < front.size() ? front[x] : back[x - front.size()]) << '\n';
            continue;
        }
        if (front.size() < back.size()) {
            front.push_back(back.front());
            back.pop_front();
        } else if (front.size() - 1 > back.size()) {
            back.push_front(front.back());
            front.pop_back();
        }
    }
    return 0;
}
