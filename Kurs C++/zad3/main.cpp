#include <iostream>
#include "number.hpp"

using namespace std;

void showNumbers(const Number &a , const Number &b,  const Number &c,  const Number &d, const Number &e);
void showHistory(const Number &n);

int main() {
    Number a(10);
    Number b = 15;
    Number c(b);
    Number d = b;
    Number e = move(Number(10));
    showNumbers(a,b,c,d,e);
    cout << endl;

    a = 7; b = 8; c = 9; d = 10; e = 11;
    showNumbers(a,b,c,d,e);
    cout << "Historia a: "; showHistory(a);
    cout << "Historia b: "; showHistory(b);
    cout << "Historia c: "; showHistory(c);
    cout << "Historia d: "; showHistory(d);
    cout << "Historia e: "; showHistory(e);
    cout << endl;

    a = 100; b = 200; c = 300; d = 400; e = 500;
    showNumbers(a,b,c,d,e);
    cout << "Historia a: "; showHistory(a);
    cout << "Historia b: "; showHistory(b);
    cout << "Historia c: "; showHistory(c);
    cout << "Historia d: "; showHistory(d);
    cout << "Historia e: "; showHistory(e);
    cout << endl;

    a.Undo(); b.Undo(); c.Undo(); d.Undo(); e.Undo();
    showNumbers(a,b,c,d,e);
    cout << "Historia a: "; showHistory(a);
    cout << "Historia b: "; showHistory(b);
    cout << "Historia c: "; showHistory(c);
    cout << "Historia d: "; showHistory(d);
    cout << "Historia e: "; showHistory(e);
    cout << endl;

    return 0;
}

void showNumbers(const Number &a , const Number &b,  const Number &c,  const Number &d, const Number &e) {
    cout << "Wartosci a/b/c/d/e: " << a.getValue() << " " << b.getValue()
         << " " << c.getValue() << " " <<  d.getValue() << " " <<  e.getValue() << endl;
};

void showHistory(const Number &n) {
    double* history = n.getHistory();
    for (int i = 0; i < 3; ++i) {
        cout << history[i] << " ";
    }
    cout << endl;
}
