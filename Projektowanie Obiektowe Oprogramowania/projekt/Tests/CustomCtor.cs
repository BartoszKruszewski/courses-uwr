public class CustomCtor
{
    public string Used;

    public CustomCtor() => Used = "default";

    [DependencyConstructor]
    public CustomCtor(string s) => Used = s;
}
