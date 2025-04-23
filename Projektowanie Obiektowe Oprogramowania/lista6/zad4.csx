#r "System.Core.dll"
using System;
using System.Linq;
using System.Linq.Expressions;

class PrintExpressionVisitor : ExpressionVisitor
{
    protected override Expression VisitBinary(BinaryExpression e)
    {
        Console.WriteLine($"[Binary] {e.Left} {e.NodeType} {e.Right}");
        return base.VisitBinary(e);
    }
    protected override Expression VisitLambda<T>(Expression<T> e)
    {
        Console.WriteLine($"[Lambda] {string.Join(", ", e.Parameters)} -> {e.Body}");
        return base.VisitLambda(e);
    }
    protected override Expression VisitConstant(ConstantExpression e)
    {
        Console.WriteLine($"[Constant] {e.Value}");
        return base.VisitConstant(e);
    }
    protected override Expression VisitParameter(ParameterExpression e)
    {
        Console.WriteLine($"[Parameter] {e.Name} : {e.Type}");
        return base.VisitParameter(e);
    }
    protected override Expression VisitUnary(UnaryExpression e)
    {
        Console.WriteLine($"[Unary] {e.NodeType} {e.Operand}");
        return base.VisitUnary(e);
    }
}

var v = new PrintExpressionVisitor();

v.Visit((Expression<Func<int, int>>)(n => 4 * (7 + n)));
v.Visit(Expression.Constant(42));
v.Visit(Expression.Parameter(typeof(int), "x"));
v.Visit(Expression.Negate(Expression.Constant(5)));