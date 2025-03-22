#include <iostream>
#include <tuple>

using namespace std;

tuple<int, int, int> extended_gcd(int a, int b) {
    if (b == 0) { return {1, 0, a}; }
    int x1, y1, d;
    tie(x1, y1, d) = extended_gcd(b, a % b);
    int x = y1;
    int y = x1 - (a / b) * y1;
    return {x, y, d};
}

int main() {    
    int N; cin >> N;
    
    while (N--) {
        int a, b; cin >> a >> b;
        int k, l, d;
        tie(k, l, d) = extended_gcd(a, b);
        cout << k << " " << l << " " << d << "\n";
    }
    return 0;
}
