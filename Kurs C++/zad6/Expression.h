# pragma once

#include <string>
#include <vector>

class Expression {
public:
    Expression(const Expression& other) = delete;
    Expression& operator=(const Expression& other) = delete;
    Expression() = default;
    virtual double eval() const = 0;
    virtual std::string toString() const = 0;
    void setPriority(uint8_t value);
    uint8_t getPriority() const;
    void setCombined(uint8_t value);
    uint8_t getCombined() const;
    Expression* operator=(Expression* other) = delete;
private:
    uint8_t priority = 7;
    // 0 - niełączny, 1 - prawostronnie, 2 - lewostronnie, 3 - całkowicie
    uint8_t combined = 0;

};

class Number final : public Expression {
public:
    explicit Number(double value);
    double eval() const override;
    std::string toString() const override;
private:
    double value;
};

class Const : public Expression {

};

class Pi final : public Const {
public:
    double eval() const override;
    std::string toString() const override;
};

class E final : public Const {
public:
    double eval() const override;
    std::string toString() const override;
};

class Fi final : public Const {
public:
    double eval() const override;
    std::string toString() const override;
};

class Var final : public Expression {
public:
    explicit Var(std::string name);

    double eval() const override;
    std::string toString() const override;

    static void addValuation(std::string name, double value);
    static void removeValuation(std::string name);
    static void modifyValuation(std::string name, double value);


private:
    static std::vector<std::pair<std::string, double>> valuations;
    std::string name;

};
