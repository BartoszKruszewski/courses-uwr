#include <bits/stdc++.h>

using namespace std;

const int MAX_L = 10007;
const int MAX_K = 107;
int freqs[MAX_L];
int dp[MAX_K][MAX_L];
int k, l;
int sum[MAX_L];
int modifiers[MAX_L];

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cin >> k >> l;

    // wczytywanie
    for (int i = 0; i < l; i++) {
        cin >> freqs[i];
    }

    // wypelnanie tablicy bez przedzialow dp[0]
    for (int i = 0; i < l; i++) {
        dp[0][i] = 0;
        for (int j = 0; j < l; j++) {
            dp[0][i] += freqs[j] * (j + 1);
        }
    }
    
    // obliczenie sum elementow od indeksu l do konca
    sum[l - 1] = freqs[l - 1];
    for (int i = l - 2; i >= 0; i--) {
        sum[i] = sum[i + 1] + freqs[i];
    }

    int m, x;
    // wypelnianie reszty dp
    for (int i = 1; i < k; i++) {
        for (int j = i; j < l; j++) {
            m = INT_MAX;
            for (int u = i - 1; u < j; u++) {
                x = dp[i - 1][u] - (j - u) * sum[j];
                if (x < m) {
                    m = x;
                } 
            }
            dp[i][j] = m;
        }
    }

    // wypisywanie dp
    cout << endl;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < l; j++) {
            cout << dp[i][j] << " ";
        }
        cout << endl;
    }

    // inicjacja tablicy przedzialow
    int bars[k + 1];
    bars[0] = 0;
    bars[k] = l;

    // szukanie wyniku (min z dp[k - 1])
    m = INT_MAX;
    for (int i = k - 1; i < l; i++) {
        if (dp[k - 1][i] < m) {
            m = dp[k - 1][i];
            bars[k - 1] = i;
        } 
    }

    // wypisywanie wyniku
    cout << endl << m << endl;

    int pre = m;
    for (int i = k - 2; i > 0; i--) {
        
        m = INT_MAX;
        for (int j = i; j < bars[i + 1]; j++) {
            x = dp[i][j] - (bars[i + 1] - j) * sum[bars[i + 1]];
            if (x == pre) {
                bars[i] = j;
                pre = dp[i][j];
                break;
            }
        }
    }

    // // wypisywanie przedzialow
    // for (int i = 0; i < k + 1; i++) {
    //     cout << bars[i] << " ";
    // }
    // cout << endl;

    // wypisywanie przedzialow
    for (int i = 0; i < k; i++) {
        cout << bars[i + 1] - bars[i] << " ";
    }
    cout << endl;
    return 0;
}