public abstract class AbstractPersonRegistry
{
    public ILoader loader;
    public List<Person> GetPersons()
    {
        return loader.Load();
    }

    public abstract void NotifyPersons();
}
public interface ILoader
{
    List<Person> Load();
}
public class Person { }