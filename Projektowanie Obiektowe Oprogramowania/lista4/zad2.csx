#load "TestRunner.csx"
#r "nuget: MSTest.TestFramework, 3.1.0"
#r "nuget: MSTest.TestAdapter, 3.1.0"

using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;

public interface IShape
{
    double Area();
}

public class Square : IShape
{
    private double _side;
    public Square(double side) => _side = side;
    public double Area() => _side * _side;
}

public class Rectangle : IShape
{
    private double _width, _height;
    public Rectangle(double width, double height)
    {
        _width = width;
        _height = height;
    }
    public double Area() => _width * _height;
}

public interface IShapeFactoryWorker
{
    string ShapeName { get; }
    IShape Create(params object[] parameters);
}

public class SquareFactoryWorker : IShapeFactoryWorker
{
    public string ShapeName => "Square";
    public IShape Create(params object[] parameters)
    {
        double side = Convert.ToDouble(parameters[0]);
        return new Square(side);
    }
}

public class RectangleFactoryWorker : IShapeFactoryWorker
{
    public string ShapeName => "Rectangle";
    public IShape Create(params object[] parameters)
    {
        double width = Convert.ToDouble(parameters[0]);
        double height = Convert.ToDouble(parameters[1]);
        return new Rectangle(width, height);
    }
}

public class ShapeFactory
{
    private readonly Dictionary<string, IShapeFactoryWorker> _workers = new();

    public void RegisterWorker(IShapeFactoryWorker worker)
    {
        _workers[worker.ShapeName] = worker;
    }

    public IShape CreateShape(string shapeName, params object[] parameters)
    {
        if (_workers.TryGetValue(shapeName, out var worker))
        {
            return worker.Create(parameters);
        }

        throw new InvalidOperationException($"Shape '{shapeName}' is not registered.");
    }
}

[TestClass]
public class Tests
{
    [TestMethod]
    public void CanCreateSquare()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new SquareFactoryWorker());

        var shape = factory.CreateShape("Square", 4);
        Assert.AreEqual(16, shape.Area(), 0.001);
    }

    [TestMethod]
    public void CanCreateRectangle()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new RectangleFactoryWorker());

        var shape = factory.CreateShape("Rectangle", 3, 5);
        Assert.AreEqual(15, shape.Area(), 0.001);
    }

    [TestMethod]
    public void ThrowsExceptionWhenShapeNotRegistered()
    {
        var factory = new ShapeFactory();

        Assert.ThrowsException<InvalidOperationException>(() =>
        {
            factory.CreateShape("Triangle", 3, 4, 5);
        });
    }

    [TestMethod]
    public void CanRegisterMultipleWorkers()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new SquareFactoryWorker());
        factory.RegisterWorker(new RectangleFactoryWorker());

        var square = factory.CreateShape("Square", 2);
        var rect = factory.CreateShape("Rectangle", 2, 4);

        Assert.AreEqual(4, square.Area(), 0.001);
        Assert.AreEqual(8, rect.Area(), 0.001);
    }

    [TestMethod]
    public void CanOverrideExistingWorker()
    {
        var factory = new ShapeFactory();
        factory.RegisterWorker(new RectangleFactoryWorker());

        factory.RegisterWorker(new RectangleFactoryWorker());

        var shape = factory.CreateShape("Rectangle", 2, 3);
        Assert.AreEqual(6, shape.Area(), 0.001);
    }
}

var tests = new Tests();

Run(tests.CanCreateSquare);
Run(tests.CanCreateRectangle);
Run(tests.ThrowsExceptionWhenShapeNotRegistered);
Run(tests.CanRegisterMultipleWorkers);
Run(tests.CanOverrideExistingWorker);
