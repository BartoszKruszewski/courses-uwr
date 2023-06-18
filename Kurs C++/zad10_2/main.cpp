#include <iostream>
#include <stdexcept>
#include "FileInput.hpp"
#include "FileOutput.hpp"

int main()
{
    std::string filename = "test.bin";
    {
        FileOutput out(filename);
        out.write(42);
        out.write(123);
        out.write(85);
    }

    {
        FileInput in1(filename);

        int a, b, c;

        in1.read(a);
        in1.read(b);
        in1.read(c);

        std::cout << "Liczby odczytane z pliku:" << std::endl;
        std::cout << a << std::endl;
        std::cout << b << std::endl;
        std::cout << c << std::endl;
    }

    {
        FileInput in2(filename);

        std::cout << "Odczytywanie pliku bajt po bajcie:" << std::endl;

        unsigned char byte;
        do {
            in2.read(byte);
            std::cout << "Wartosc: " << static_cast<int>(byte);
            std::cout << " Hex: " << std::hex << static_cast<int>(byte);
            std::cout << " Znak: ('" << static_cast<char>(byte) << "')" << std::endl;
        } while (!in2.eof());
    }

    return 0;
}

