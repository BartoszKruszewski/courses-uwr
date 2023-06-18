#include <iostream>
#include <vector>
#include <algorithm>
#include "Manipulators.h"

bool ignoreCaseCompare(const std::string &str1, const std::string &str2) {
    std::string str1Lower, str2Lower;
    std::transform(str2.begin(), str2.end(), std::back_inserter(str2Lower), ::tolower);
    return str1Lower < str2Lower;
}

std::ostream &operator<<(std::ostream &os, const IndexManipulator &manipulator) {
    os << "[" << std::setw(manipulator.w) << manipulator.x << "]";
    return os;
}

std::istream &operator>>(std::istream &is, const IndexIgnore &manipulator) {
    char c;
    int count = 0;
    while (count < manipulator.x && is.get(c) && c != '\n') {
        count++;
    }
    return is;
}

void testSort() {
    std::vector<std::string> lines;
    std::string line;

    while (std::getline(std::cin, line) && !line.empty()) {
        lines.push_back(line);
    }

    std::sort(lines.begin(), lines.end(), ignoreCaseCompare);

    for (int i = 0; i < lines.size(); i++) {
        std::cout << index(i, 2) << colon << lines[i] << '\n';
    }
}

int main() {

    testSort();

    std::string line;

    std::cout << "Podaj dwie linie:" << std::endl;
    while (std::getline(std::cin, line)) {
        std::cout << "Wprowadzono: " << line << '\n';
    }

    std::cout << "Podaj linie:" << std::endl;
    std::cin >> ignore(3) >> line;
    std::cout << "Linia bez 3 pierwszych znakow, poprzedona przecikiem: " << comma << line << std::endl;

    return 0;
}

