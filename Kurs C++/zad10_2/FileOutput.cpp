#include "FileOutput.hpp"

FileOutput::FileOutput(const std::string &filename) {
    try {
        file.open(filename, std::ios::binary);
    }
    catch (const std::exception& e) {
        throw e;
    }
}
FileOutput::~FileOutput() {
    if (file.is_open()) {
        file.close();
    }
}

