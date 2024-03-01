#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (a > b) swap(a, b);
    for (int i = a; i <= b; i++) cout << i << endl;
    return 0;
}