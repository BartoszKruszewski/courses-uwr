#pragma once
#include "OperatorSingleArg.h"

class OperatorDualArg : public OperatorSingleArg {
public:
    virtual std::string toString() const override;
protected:
    explicit OperatorDualArg(Expression* expression1, Expression* expression2);;
    virtual void setArg2(Expression* expression);
    Expression* getArg2() const;
private:
    Expression* arg2;
};

class Sum final : public OperatorDualArg {
public:
    Sum(Expression* expression1, Expression* expression2);;
    double eval() const override;
};

class Diff final : public OperatorDualArg {
public:
    Diff(Expression* expression1, Expression* expression2);;
    double eval() const override;
};

class Prod final : public OperatorDualArg {
public:
    Prod(Expression* expression1, Expression* expression2);;
    double eval() const override;
};

class Div final : public OperatorDualArg {
public:
    Div(Expression* expression1, Expression* expression2);;
    double eval() const override;
};

class Log final : public OperatorDualArg {
public:
    Log(Expression* expression1, Expression* expression2);
    double eval() const override;
    std::string toString() const override;
};

class Mod final : public OperatorDualArg {
public:
    Mod(Expression* expression1, Expression* expression2);
    double eval() const override;
};

class Pow final : public OperatorDualArg {
public:
    Pow(Expression* expression1, Expression* expression2);;
    double eval() const override;
};
