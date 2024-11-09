using System.Collections.Generic;
using System.Web;

public class DataContextProvider
{
    private const string DataContextKey = "DataContext";

    public static List<ExampleEntity> GetDataContext(HttpContext context)
    {
        if (context.Session[DataContextKey] == null)
        {
            context.Session[DataContextKey] = new List<ExampleEntity>();
        }

        return (List<ExampleEntity>)context.Session[DataContextKey];
    }
}