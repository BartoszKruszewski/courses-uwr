#include <iostream>
#include <vector>
using namespace std;

const int MAXX = 1000000;
vector<int> phi(MAXX + 1);

void precompute_phi() {
    for (int i = 0; i <= MAXX; i++) {
        phi[i] = i;
    }

    for (int i = 2; i <= MAXX; i++) {
        if (phi[i] == i) {  // i jest liczbą pierwszą
            for (int j = i; j <= MAXX; j += i) {
                phi[j] = (phi[j] / i) * (i - 1);
            }
        }
    }
}

int main() {
    precompute_phi();

    int N; cin >> N;

    while (N--) {
        int x; cin >> x;
        cout << phi[x] << "\n";
    }
    return 0;
}