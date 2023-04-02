#include "number.hpp"
#include <stdexcept>


Number::Number(double value) {
    this->history = new double[historySize];
    this->actualValue = value;
    this->saveActualValue();
}

Number::Number(const Number &other) noexcept
        : history(new double[historySize]),
          actualValue(other.actualValue),
          actualHistorySteps(0),
          actualHistoryIndex(0) {
}

Number::Number(Number &&other) noexcept {
    this->history = other.history;
    this->actualValue = other.actualValue;
    this->actualHistorySteps = other.actualHistorySteps;
    this->actualHistoryIndex = other.actualHistoryIndex;
    other.history = nullptr;
}


Number::Number() : Number(0) {}

Number::~Number() {
    if (this->history != nullptr) {
        delete[] this->history;
    }

}

double Number::getValue() const {
    return this->actualValue;
}

double *Number::getHistory() const {
    return this->history;
}

void Number::Undo() {
    if (this->actualHistorySteps > 0) {
        this->actualHistorySteps--;
        this->actualHistoryIndex--;
        if (this->actualHistoryIndex < 0) {
            this->actualHistoryIndex = this->historySize - 1;
        }
        this->actualValue = this->history[this->actualHistoryIndex];
    }
}

void Number::saveActualValue() {
    if (this->actualHistorySteps < this->historySize - 1) {
        this->actualHistorySteps++;
    }
    this->actualHistoryIndex++;
    if (this->actualHistoryIndex == this->historySize) {
        this->actualHistoryIndex = 0;
    }
    this->history[this->actualHistoryIndex] = actualValue;
}

Number Number::operator=(double value) {
    this->actualValue = value;
    saveActualValue();
    return *this;
}

Number Number::operator=(const Number &other) {
    this->actualValue = other.actualValue;
    this->history = new double[historySize];
    actualHistoryIndex = other.actualHistoryIndex;
    actualHistorySteps = other.actualHistorySteps;
    for (int i = 0; i < historySize; i++) {
        this->history[i] = other.history[i];
    }
    return *this;
}

Number Number::operator=(Number &&other) {
    this->actualValue = other.actualValue;
    this->history = other.history;
    actualHistoryIndex = other.actualHistoryIndex;
    actualHistorySteps = other.actualHistorySteps;
    other.history = nullptr;
    return *this;
}

