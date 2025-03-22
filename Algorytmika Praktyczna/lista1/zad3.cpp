#include <iostream>
#include <vector>
using namespace std;

const int MAXX = 1000000;
vector<int> divisors_count(MAXX + 1, 0);

void precompute_divisors() {
    for (int i = 1; i <= MAXX; i++) {
        for (int j = i; j <= MAXX; j += i) {
            divisors_count[j]++;
        }
    }
}

int main() {
    precompute_divisors();

    int N; cin >> N;
    while (N--) {
        int x; cin >> x;
        cout << divisors_count[x] << "\n";
    }

    return 0;
}