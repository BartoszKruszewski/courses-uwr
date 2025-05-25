public class A
{
    public B BDep { get; }
    public A(B b) => BDep = b;
}
