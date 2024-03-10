#include <bits/stdc++.h>
using namespace std;

#define K 2
#define val first

vector<int> L[K] = {
    {2, 3, 5},
    {10, 11, 13},
};

pair<int, int> solve() {
    int list_counter[K];
    deque<pair<int, int>> ACTUAL;

    for (int i = 0; i < K; i++) ACTUAL.push_back({L[i][0], i});
    for (int i = 0; i < K; i++) list_counter[i] = 1;

    sort(ACTUAL.begin(), ACTUAL.end());

    int a = ACTUAL.front().val;
    int r = ACTUAL.back().val;

    while (true) {
        auto [v, k] = ACTUAL.front();
        ACTUAL.pop_front();

        if (list_counter[k] == L[k].size()) break;
        ACTUAL.push_back({L[k][list_counter[k]], k});
        list_counter[k]++;

        sort(ACTUAL.begin(), ACTUAL.end());

        if (ACTUAL.back().val - ACTUAL.front().val < r - a) {
            a = ACTUAL.front().val;
            r = ACTUAL.back().val;
        } 
    }

    return {a, r};
}

int main() {
    auto [a, r] = solve();
    cout << a << " " << r << endl;
}