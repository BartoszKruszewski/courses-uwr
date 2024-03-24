#include <bits/stdc++.h>
using namespace std;

struct Coin {
    double p, w;
};

void knapSack(int f, Coin coins[], int n, bool reversed) {
    int amounts[n];
    memset(amounts, 0, sizeof(amounts));
    int w = 0;
    int p = 0;
    int i = 0;

    while (w < f && i < n) {
        if (w + coins[i].w <= f) {
            w += coins[i].w;
            p += coins[i].p;
            amounts[i] += 1;
        }
        else {
            i++;
        }
    }
    if (reversed) {
        if (w == f) cout << "TAK" << endl;
        else cout << "NIE" << endl;
    }
    if (w == f) {
        cout << p << endl;
        if (reversed) for (int i = n - 1; i >= 0; i--) cout << amounts[i] << " ";
        else for (int i = 0; i < n; i++) cout << amounts[i] << " ";
        cout << endl;
    }
}

int main() {
    int f, n;
    cin >> f >> n;
    Coin coins[n];
    for (int i = 0; i < n; i++) {
        cin >> coins[i].p >> coins[i].w;
    }
    sort(coins, coins + n, [](Coin a, Coin b) {return a.p / a.w < b.p / b.w;});
    knapSack(f, coins, n, true);
    sort(coins, coins + n, [](Coin a, Coin b) {return a.p / a.w > b.p / b.w;});
    knapSack(f, coins, n, false);
    return 0;
}