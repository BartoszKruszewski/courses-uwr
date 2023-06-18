#pragma once
#include "Expression.h"

class OperatorSingleArg : public Expression {
public:
    virtual std::string toString() const override;
protected:
    explicit OperatorSingleArg(Expression* expression);
    virtual void setArg1(Expression* expression);
    void setOperatorSymbol(std::string symbol);
    std::string getOperatorSymbol() const;
    Expression* getArg1() const;
private:
    std::string operatorSymbol;
    Expression* arg1;
};

class Sin final : public OperatorSingleArg {
public:
    Sin(Expression* expression);;
    double eval() const override;
};

class Cos final : public OperatorSingleArg {
public:
    Cos(Expression* expression);;
    double eval() const override;
};

class Exp final : public OperatorSingleArg {
public:
    Exp(Expression* expression);;
    double eval() const override;
};

class Ln final : public OperatorSingleArg {
public:
    Ln(Expression* expression);
    double eval() const override;
};

class Abs final : public OperatorSingleArg {
public:
    Abs(Expression* expression);;
    double eval() const override;
};

class Opp final : public OperatorSingleArg {
public:
    Opp(Expression* expression);;
    double eval() const override;
};

class Inv final : public OperatorSingleArg {
public:
    Inv(Expression* expression);
    double eval() const override;
};