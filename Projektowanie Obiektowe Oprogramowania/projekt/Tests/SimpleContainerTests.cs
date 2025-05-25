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
    public void ThrowsOnUnregisteredInterface()
    {
        Assert.ThrowsException<System.InvalidOperationException>(() =>
        {
            container.Resolve<IFoo>();
        });
    }

    [TestMethod]
    public void RegisterInstance_ReturnsSameInstance()
    {
        var container = new SimpleContainer();
        var foo = new Foo();
        container.RegisterInstance<IFoo>(foo);

        var resolved1 = container.Resolve<IFoo>();
        var resolved2 = container.Resolve<IFoo>();

        Assert.AreSame(foo, resolved1);
        Assert.AreSame(foo, resolved2);
    }

    [TestMethod]
    public void Resolve_InjectsSimpleDependency()
    {
        var container = new SimpleContainer();
        var a = container.Resolve<A>();

        Assert.IsNotNull(a);
        Assert.IsNotNull(a.BDep);
    }

    [TestMethod]
    public void Resolve_InjectsRegisteredInterface()
    {
        var container = new SimpleContainer();
        container.RegisterType<IC, C>();

        var a = container.Resolve<A2>();

        Assert.IsNotNull(a.CDep);
        Assert.IsInstanceOfType(a.CDep, typeof(C));
    }

    [TestMethod]
    public void Resolve_InjectsRegisteredPrimitiveInstance()
    {
        var container = new SimpleContainer();
        container.RegisterInstance("ala ma kota");

        var obj = container.Resolve<WithString>();

        Assert.AreEqual("ala ma kota", obj.S);
    }

    [TestMethod]
    [ExpectedException(typeof(InvalidOperationException))]
    public void Resolve_Throws_WhenUnknownParameterCannotBeInjected()
    {
        var container = new SimpleContainer();
        container.Resolve<WithString>(); // string nie został zarejestrowany
    }

    [TestMethod]
    [ExpectedException(typeof(InvalidOperationException))]
    public void Resolve_Throws_WhenCyclicDependencyDetected()
    {
        var container = new SimpleContainer();
        container.Resolve<LoopA>();
    }

    [TestMethod]
    public void Resolve_UsesMarkedDependencyConstructor()
    {
        var container = new SimpleContainer();
        container.RegisterInstance("Hello");

        var obj = container.Resolve<CustomCtor>();

        Assert.AreEqual("Hello", obj.Used);
    }
}