#pragma once
#include <fstream>

class FileOutput {
public:
    FileOutput(const std::string& filename);
    ~FileOutput();

    template<typename T>
    void write(const T& value)
    {
        file.write(reinterpret_cast<const char*>(&value), sizeof(T));
    }

private:
    std::ofstream file;
};

