// dotnet script zad4.cs

var calc = new AreaCalculator();

IShape rect = new Rectangle(4, 5);
Console.WriteLine($"Pole prostokąta: {calc.CalculateArea(rect)}");

IShape sq = new Square(4);
Console.WriteLine($"Pole kwadratu: {calc.CalculateArea(sq)}"); 

public interface IShape
{
    int CalculateArea();
}

public class Rectangle : IShape
{
    // Zamiast set-ów mamy konstruktor i tylko gettery
    public int Width { get; }
    public int Height { get; }

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    public int CalculateArea()
    {
        return Width * Height;
    }
}

public class Square : IShape
{
    // Kwadrat ma jeden wymiar: side
    public int Side { get; }

    public Square(int side)
    {
        Side = side;
    }

    public int CalculateArea()
    {
        return Side * Side;
    }
}

public class AreaCalculator
{
    public int CalculateArea(IShape shape)
    {
        return shape.CalculateArea();
    }
}
