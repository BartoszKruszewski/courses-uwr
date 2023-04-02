#include "TabBit.hpp"
#include "cmath"
#include <iostream>
#include <string>
#include <stdexcept>

istream &operator>>(istream &in, TabBit &tb) {
    string val;
    in >> val;
    try {
        int index = std::stoi(val);
        if (index >= 0 && index < tb.len) {
            tb[index] = true;
        }
        else {
            throw std::invalid_argument("Podana wartosc jest wieksza od wielkosci tablicy!");
        }
    }
    catch (std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
    catch (...) {
        cerr << "Podana wartosc nie jest liczba!" << std::endl;
    }
    return in;
}

ostream &operator<<(ostream &out, const TabBit &tb) {
    string result = "";
    for (int i = 0; i<tb.size(); i++) {
        result += tb[i] ? "1" : "0" ;
        result += " ";
    }
    out << result;
    return out;
}

TabBit::TabBit(int size) {
    len = size;
    tab = new TabBit::word[len/wordSize + 1];
    for (int i = 0; i<len/wordSize + 1; i++) {
        tab[i] = 0;
    }
}

TabBit::TabBit(TabBit::word tb) {
    len = wordSize;
    tab = new TabBit::word[1];
    tab[0] = tb;
}

TabBit::TabBit(const TabBit &tb) {
    len = tb.len;
    tab = new TabBit::word[len/wordSize + 1];
    for (int i = 0; i<len/wordSize + 1; i++) {
        tab[i] = tb.tab[i];
    }
}

TabBit::TabBit(TabBit &&tb) noexcept {
    len = tb.len;
    tab = new TabBit::word[len/wordSize + 1];
    for (int i = 0; i<len/wordSize + 1; i++) {
        tab[i] = tb.tab[i];
    }
    for (int i = 0; i<len/wordSize + 1; i++) {
        tb.tab[i] = 0;
    }
}

TabBit &TabBit::operator=(const TabBit &tb) {
    len = tb.len;
    tab = new TabBit::word[len/wordSize + 1];
    for (int i = 0; i<len/wordSize + 1; i++) {
        tab[i] = tb.tab[i];
    }
    return *this;
}

TabBit &TabBit::operator=(TabBit &&tb) noexcept {
    len = tb.len;
    tab = new TabBit::word[len/wordSize + 1];
    for (int i = 0; i<len/wordSize + 1; i++) {
        tab[i] = tb.tab[i];
    }
    for (int i = 0; i<len/wordSize + 1; i++) {
        tb.tab[i] = 0;
    }
    return *this;
}

TabBit::~TabBit() {
    if (tab != nullptr) {
        delete tab;
    }
}

bool TabBit::read(int index) const {
    word w = tab[index / wordSize];
    w >>= index % wordSize;
    return w & 1;
}

void TabBit::write(int index, bool b) {
    if (b) {
        tab[index / wordSize] |= (1 << (index % wordSize));
    } else {
        tab[index / wordSize] &= ~(1 << (index % wordSize));
    }
}

bool TabBit::operator[](int i) const {
    if (i >= size()) {
        throw std::invalid_argument("Podana wartosc jest wieksza od wielkosci tablicy!");
    }
    return read(i);
}

TabBit::ref TabBit::operator[](int i) {
    if (i >= size()) {
        throw std::invalid_argument("Podana wartosc jest wieksza od wielkosci tablicy!");
    }
    return ref(tab[i/wordSize], i % wordSize);
}

int TabBit::size() const {
    return len;
}

TabBit TabBit::operator|(const TabBit &tb) const {
    if (len != tb.size()) {
        throw std::invalid_argument("Tablice sa roznej dlugosci!");
    }
    TabBit newTab(tb.size());
    for (int i = 0; i<len; i++) {
        newTab[i] = read(i) || tb[i];
    }
    return newTab;
}

TabBit &TabBit::operator|=(const TabBit &tb) {
    if (len != tb.size()) {
        throw std::invalid_argument("Tablice sa roznej dlugosci!");
    }
    for (int i = 0; i<len; i++) {
        tab[i] = read(i) || tb[i];
    }
    return *this;
}

TabBit TabBit::operator&(const TabBit &tb) const {
    if (len != tb.size()) {
        throw std::invalid_argument("Tablice sa roznej dlugosci!");
    }
    TabBit newTab(tb.size());
    for (int i = 0; i<len; i++) {
        newTab[i] = read(i) && tb[i];
    }
    return newTab;
}

TabBit &TabBit::operator&=(const TabBit &tb) {
    if (len != tb.size()) {
        throw std::invalid_argument("Tablice sa roznej dlugosci!");
    }
    for (int i = 0; i<len; i++) {
        tab[i] = read(i) && tb[i];
    }
    return *this;
}

TabBit TabBit::operator^(const TabBit &tb) const {
    if (len != tb.size()) {
        throw std::invalid_argument("Tablice sa roznej dlugosci!");
    }
    TabBit newTab(tb.size());
    for (int i = 0; i<len; i++) {
        newTab[i] = read(i) != tb[i];
    }
    return newTab;
}

TabBit &TabBit::operator^=(const TabBit &tb) {
    if (len != tb.size()) {
        throw std::invalid_argument("Tablice sa roznej dlugosci!");
    }
    for (int i = 0; i<len; i++) {
        tab[i] = read(i) != tb[i];
    }
    return *this;
}

TabBit TabBit::operator!() const {
    TabBit newTab(len);
    for (int i = 0; i<len; i++) {
        newTab[i] = !(read(i));
    }
    return newTab;
}

TabBit::TabBit(std::initializer_list<bool> l) : TabBit((int)l.size()){
    int i = 0;
    for (bool x : l) {
        write(i++, x);
    }
}


TabBit::ref::ref(TabBit::word &wordRef, int bitIndex) : wordRef(wordRef), bitIndex(bitIndex) {}

TabBit::ref::operator bool() const {
    return (wordRef & (1 << bitIndex)) != 0;
}

TabBit::ref &TabBit::ref::operator=(bool b) {
    if (b) {
        wordRef |= (1 << bitIndex);
    } else {
        wordRef &= ~(1 << bitIndex);
    }
    return *this;
}
