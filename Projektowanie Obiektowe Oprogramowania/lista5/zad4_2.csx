public abstract class AbstractPersonRegistry
{
    public IMessenger messenger;
    public abstract List<Person> GetPersons();
    public void NotifyPersons()
    {
        foreach (Person person in GetPersons())
            messenger.Notify(person);
    }
}
public interface IMessenger
{
    void Notify(Person person);
}
public class Person { }