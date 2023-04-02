#pragma once

#include <iostream>

using namespace std;

class TabBit {
private:
    typedef uint16_t word; // komorka w tablicy
    int len; // liczba bitów
    word *tab; // tablica bitów
    static const int wordSize = 16; // rozmiar slowa w bitach
    friend istream &operator>>(istream &in, TabBit &tb);

    friend ostream &operator<<(ostream &out, const TabBit &tb);

    //klasa ref
    class ref {
        word &wordRef;
        int bitIndex;

    public:
        ref(word &wordRef, int bitIndex);;

        operator bool() const;

        ref &operator=(bool b);
    };

public:
    explicit TabBit(int size); // wyzerowana tablica bitow [0...rozm]
    explicit TabBit(word tb); // tablica bitów [0...rozmiarSlowa] zainicjalizowana wzorcem
    TabBit(const TabBit &tb); // konstruktor kopiujący
    TabBit(TabBit &&tb) noexcept; // konstruktor przenoszący
    TabBit(std::initializer_list<bool> l);

    TabBit &operator=(const TabBit &tb); // przypisanie kopiujące
    TabBit &operator=(TabBit &&tb) noexcept; // przypisanie przenoszące
    ~TabBit(); // destruktor
private:
    bool read(int index) const; // metoda pomocnicza do odczytu bitu
    void write(int index, bool b); // metoda pomocnicza do zapisu bitu
public:
    bool operator[](int i) const; // indeksowanie dla stałych tablic bitowych
    ref operator[](int i);

    inline int size() const; // rozmiar tablicy w bitach

public:
    TabBit operator|(const TabBit &tb) const;

    TabBit &operator|=(const TabBit &tb);

    TabBit operator&(const TabBit &tb) const;

    TabBit &operator&=(const TabBit &tb);

    TabBit operator^(const TabBit &tb) const;

    TabBit &operator^=(const TabBit &tb);

    TabBit operator!() const;
};
