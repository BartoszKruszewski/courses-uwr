class Program
{
    static void Main()
    {
        var container = new SimpleContainer();

        container.RegisterType<IFoo, Foo>(false);
        var foo1 = container.Resolve<IFoo>();
        
        container.RegisterType<IFoo, Bar>(false);
        var foo2 = container.Resolve<IFoo>();

        container.RegisterType<Foo>(true);
        var f1 = container.Resolve<Foo>();
        var f2 = container.Resolve<Foo>();

        System.Console.WriteLine(foo1.GetType().Name);
        System.Console.WriteLine(foo2.GetType().Name);
        System.Console.WriteLine(object.ReferenceEquals(f1, f2));
    }
}