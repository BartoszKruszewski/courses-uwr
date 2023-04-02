#include <iostream>
#include "TabBit.hpp"

int main() {
    TabBit tab {1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
                0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0};
    std::cout << "tab: " << tab << endl;
    std::cout << "!tab: " << !tab << endl;
    std::cout << "tab & tab: " << (tab & tab) << endl;
    std::cout << "!tab & !tab: " << (!tab & !tab) << endl;
    std::cout << "tab | tab " << (tab | tab) << endl;
    std::cout << "tab | !tab " << (tab | !tab) << endl;
    std::cout << "tab ^ tab: " << (tab ^ tab) << endl;
    std::cout << "tab ^ !tab: " << (tab ^ !tab) << endl;
    std::cout << "tab.size(): " << tab.size() << endl;


    TabBit t1 = tab;
    cout << "t1 = tab: " << t1 << endl;
    TabBit t2 = std::move(t1);
    cout << "t2 = move(t1): "  << t2 << endl;
    cout << "t1: " << t1 << endl;

    cout << "tab[15]: " << tab[15] << endl;
    cout << "tab: " << tab << endl;
    tab[1] = 1;
    cout << "tab[1] = 1: " << tab << endl;
    cin >> tab;
    cout << "tab: " << tab << endl;

    return 0;
}
