#ifndef NUMBER_HPP
#define NUMBER_HPP


class Number {
public:
    Number(double value);
    Number(const Number &other) noexcept;
    Number(Number &&other) noexcept;
    Number();

    ~Number();
    void Undo();
    Number operator =(double value);
    Number operator =(const Number &other);
    Number operator =(Number &&other);
    double getValue() const;
    double* getHistory() const;

private:
    void saveActualValue();
    const static int historySize = 3;
    double actualValue;
    int actualHistoryIndex = 0;
    int actualHistorySteps = 0;
    double* history;
};


#endif
