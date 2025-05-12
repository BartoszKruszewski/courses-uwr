[TestClass]
public class SimpleContainerTests
{
    private SimpleContainer container = null!;

    [TestInitialize]
    public void Init()
    {
        container = new SimpleContainer();
    }

    [TestMethod]
    public void ResolvesConcreteType()
    {
        var a = container.Resolve<Foo>();
        var b = container.Resolve<Foo>();
        Assert.IsNotNull(a);
        Assert.AreNotSame(a, b);
    }

    [TestMethod]
    public void SingletonReturnsSameInstance()
    {
        container.RegisterType<Foo>(true);
        var a = container.Resolve<Foo>();
        var b = container.Resolve<Foo>();
        Assert.AreSame(a, b);
    }

    [TestMethod]
    public void ResolvesRegisteredInterface()
    {
        container.RegisterType<IFoo, Bar>(false);
        var x = container.Resolve<IFoo>();
        Assert.IsInstanceOfType(x, typeof(Bar));
    }

    [TestMethod]
    public void ThrowsOnUnregisteredInterface()
    {
        Assert.ThrowsException<System.InvalidOperationException>(() =>
        {
            container.Resolve<IFoo>();
        });
    }
}