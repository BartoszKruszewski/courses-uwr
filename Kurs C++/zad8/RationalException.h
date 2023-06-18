# pragma once
#include <stdexcept>

class RationalException : public std::logic_error {
protected:
    explicit RationalException(const std::string& message) : std::logic_error(message) {}
};

class OutOfRangeException : public RationalException {
public:
    explicit OutOfRangeException(const std::string& message) : RationalException(message) {}
};

class DivisionByZeroException : public RationalException {
public:
    explicit DivisionByZeroException(const std::string& message) : RationalException(message) {}
};
