#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000007;
const int MAXN = 1000000;
vector<long long> fact(MAXN + 1), inv_fact(MAXN + 1);

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

void precompute_factorials() {
    fact[0] = 1;
    for (int i = 1; i <= MAXN; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    inv_fact[MAXN] = mod_pow(fact[MAXN], MOD - 2, MOD);
    for (int i = MAXN - 1; i >= 0; i--) {
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD;
    }
}

long long binomial_coefficient(int a, int b) {
    if (b > a || b < 0) return 0;
    return (fact[a] * inv_fact[b] % MOD) * inv_fact[a - b] % MOD;
}

int main() {
    precompute_factorials();

    int N; cin >> N;
    
    while (N--) {
        int a, b; cin >> a >> b;
        cout << binomial_coefficient(a, b) << "\n";
    }
    return 0;
}