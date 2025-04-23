using System;
using System.Collections.Generic;

public class Context
{
    private readonly Dictionary<string, bool> _values = new();

    public bool GetValue(string name)
    {
        if (!_values.ContainsKey(name)) throw new Exception($"Brak wartości dla '{name}'");
        return _values[name];
    }

    public void SetValue(string name, bool value) => _values[name] = value;
}

public abstract class AbstractExpression
{
    public abstract bool Interpret(Context context);
}

public class ConstExpression : AbstractExpression
{
    private readonly bool _value;
    public ConstExpression(bool value) => _value = value;
    public override bool Interpret(Context context) => _value;
}

public class VariableExpression : AbstractExpression
{
    private readonly string _name;
    public VariableExpression(string name) => _name = name;
    public override bool Interpret(Context context) => context.GetValue(_name);
}

public class BinaryExpression : AbstractExpression
{
    private readonly AbstractExpression _left, _right;
    private readonly char _op;
    public BinaryExpression(AbstractExpression l, AbstractExpression r, char op) => (_left, _right, _op) = (l, r, op);
    public override bool Interpret(Context context) => _op switch
    {
        '&' => _left.Interpret(context) && _right.Interpret(context),
        '|' => _left.Interpret(context) || _right.Interpret(context),
        _ => throw new Exception("Nieznany operator")
    };
}

public class UnaryExpression : AbstractExpression
{
    private readonly AbstractExpression _expr;
    public UnaryExpression(AbstractExpression expr) => _expr = expr;
    public override bool Interpret(Context context) => !_expr.Interpret(context);
}

var ctx = new Context();
ctx.SetValue("x", false);
ctx.SetValue("y", true);

AbstractExpression exp = new BinaryExpression(
    new UnaryExpression(
        new BinaryExpression(
            new VariableExpression("x"),
            new VariableExpression("y"),
            '&'
        )
    ),
    new ConstExpression(true),
    '|'
);

Console.WriteLine(exp.Interpret(ctx));