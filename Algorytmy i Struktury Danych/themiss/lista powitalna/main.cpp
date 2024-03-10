// Bartosz Kruszewski
// 337568
// KPO

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long long a, b;
    cin >> a >> b;
    if (a % 2024 != 0) a = (a / 2024 + 1) * 2024;
    while (a <= b) {
        cout << a << " ";
        a += 2024;
    }
    return 0;
}
