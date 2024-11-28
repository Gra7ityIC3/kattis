#include <bits/stdc++.h>
#include "vectorfunctions.h"
using namespace std;

void backwards(vector<int>& vec){
    reverse(vec.begin(), vec.end());
}

vector<int> everyOther(const vector<int>& vec) {
    vector<int> ans;
    for (int i = 0; i < vec.size(); i += 2)
        ans.push_back(vec[i]);
    return ans;
}

int smallest(const vector<int>& vec) {
    return *min_element(vec.begin(), vec.end());
}

int sum(const vector<int>& vec) {
    return accumulate(vec.begin(), vec.end(), 0);
}

int veryOdd(const vector<int>& suchVector) {
    int ans = 0;
    for (int i = 1; i < suchVector.size(); i += 2)
        ans += suchVector[i] % 2;
    return ans;
}
