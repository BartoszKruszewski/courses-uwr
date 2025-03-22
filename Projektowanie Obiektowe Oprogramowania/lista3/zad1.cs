// dotnet script zad1.cs

var factory = new RectangleFactory();
Rectangle rect = factory.CreateRectangle(5, 3);
Console.WriteLine($"Area of rectangle: {rect.GetArea()}");

class Rectangle
{
    public int Width { get; }
    public int Height { get; }

    public Rectangle(int width, int height)
    {
        Width = width;
        Height = height;
    }

    // Zgodnie z zasadą Information Expert 
    // klasa, która posiada dane (Width, Height),
    // odpowiada za ich przetwarzanie (GetArea).
    public int GetArea()
    {
        return Width * Height;
    }
}

class RectangleFactory
{
    // Zgodnie z zasadą Creator
    // klasa RectangleFactory tworzy obiekty Rectangle,
    // ponieważ jest to jej główna odpowiedzialność.
    public Rectangle CreateRectangle(int width, int height)
    {
        return new Rectangle(width, height);
    }
}
