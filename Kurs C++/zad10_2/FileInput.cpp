#include "FileInput.hpp"

FileInput::FileInput(const std::string &filename) {
    try {
        file.open(filename, std::ios::binary);
    }
    catch (const std::exception& e) {
        throw e;
    }
}
FileInput::~FileInput() {
    if (file.is_open()) {
        file.close();
    }
}

bool FileInput::eof() {
    return file.eof();
}
