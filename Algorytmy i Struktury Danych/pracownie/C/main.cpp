#include <bits/stdc++.h>
using namespace std;

struct Coin {
    int idx, w, p;
};

const int MAX_F = 1000007;
const int MAX_N = 1000007;

long long dp[MAX_F];
int attachment[MAX_F];
Coin coins[MAX_N];
int amounts[MAX_N];

void maximum(int f, int n) { 
    for (int i = 0; i <= f; i++) dp[i] = LLONG_MIN;
    for (int i = 0; i <= f; i++) attachment[i] = 0;
    for (int i = 0; i < n; i++) amounts[i] = 0;

    dp[0] = 0;
    for (int i = 0; i <= f; i++) 
        for (int j = 0; j < n && coins[j].w <= i; j++) 
            if (dp[i - coins[j].w] != LLONG_MIN)
                if (dp[i - coins[j].w] + coins[j].p > dp[i]) {
                    dp[i] = dp[i - coins[j].w] + coins[j].p;
                    attachment[i] = j;
                }

    // cout << endl << endl;
    // for (int i = 0; i <= f; i++) cout << i << ", " << dp[i] << endl;
    // cout << endl << endl;

    int x = f;
    while (x > 0) {
        amounts[coins[attachment[x]].idx]++;
        x -= coins[attachment[x]].w;
    }

    if (x == 0) {
        cout << dp[f] << endl;
        for (int i = 0; i < n; i++) 
            cout << amounts[i] << " ";
        cout << endl;
    }
}

void minimum(int f, int n) {
    for (int i = 0; i <= f; i++) dp[i] = LLONG_MAX;
    for (int i = 0; i <= f; i++) attachment[i] = 0;
    for (int i = 0; i < n; i++) amounts[i] = 0;
    dp[0] = 0;
    for (int i = coins[0].w; i <= f; i++) 
        for (int j = 0; j < n && coins[j].w <= i; j++) 
            if (dp[i - coins[j].w] != LLONG_MAX)
                if (dp[i - coins[j].w] + coins[j].p < dp[i]) {
                    dp[i] = dp[i - coins[j].w] + coins[j].p;
                    attachment[i] = j;
                }

    int x = f;
    while (x > 0) {
        amounts[coins[attachment[x]].idx]++;
        x -= coins[attachment[x]].w;
    }

    if (x == 0) {
        cout << "TAK" << endl;
        cout << dp[f] << endl;
        for (int i = 0; i < n; i++) 
            cout << amounts[i] << " ";
        cout << endl;
    } else cout << "NIE" << endl;
}
  
int main()
{
    int f, n;
    cin >> f >> n;
    for (int i = 0; i < n; i++) {
        cin >> coins[i].p >> coins[i].w;
        coins[i].idx = i;
    }
    sort(coins, coins + n, [](Coin a, Coin b){return a.w < b.w;});
    minimum(f, n);
    maximum(f, n);
    return 0;
}