#include <iostream>
#include <string>
#include <vector>

using namespace std;

string bin2roman(int x);

int main(int argc, char **argv) {
    for (int i = 1; i < argc; i++) {
        size_t p;
        try {
            int number = stoi(argv[i], &p);
            string l = string(argv[i]);
            if ((p == l.length()) && (number > 0 && number < 4000)) {
                cout << bin2roman(number) << endl;
            } else {
                clog << "Argument '" << argv[i] << "' jest niepoprawny" << endl;
            }
        }
        catch (...) {
            clog << "Argument '" << argv[i] << "' jest niepoprawny" << endl;
        }
    }
    return 0;
}

string bin2roman(int x) {
    const vector<pair<int, string>> roman = {
            {1000, "M"},
            {900,  "CM"},
            {500,  "D"},
            {400,  "CD"},
            {100,  "C"},
            {90,   "XC"},
            {50,   "L"},
            {40,   "XL"},
            {10,   "X"},
            {9,    "IX"},
            {5,    "V"},
            {4,    "IV"},
            {1,    "I"}
    };

    string romanNumber;
    while (x > 0) {
        for (const pair<int, string> &r: roman) {
            if (x >= r.first) {
                x -= r.first;
                romanNumber += r.second;
                break;
            }
        }
    }
    return romanNumber;
}
