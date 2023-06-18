#pragma once
#include <fstream>

class FileInput {
public:
    FileInput(const std::string& filename);
    ~FileInput();

    template<typename T>
    void read(T& value)
    {
        file.read(reinterpret_cast<char*>(&value), sizeof(T));
    }

    bool eof();

private:
    std::ifstream file;
};

