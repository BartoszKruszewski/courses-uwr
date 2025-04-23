using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

var dbHandler = new DataAccessHandler(new DatabaseStrategy());
dbHandler.Execute();

Console.WriteLine();

var xmlHandler = new DataAccessHandler(new XmlStrategy());
xmlHandler.Execute();

interface IDataAccessStrategy
{
    void Connect();
    object GetData();
    void ProcessData(object data);
    void Disconnect();
}

class DataAccessHandler
{
    private readonly IDataAccessStrategy strategy;

    public DataAccessHandler(IDataAccessStrategy strategy)
    {
        this.strategy = strategy;
    }

    public void Execute()
    {
        strategy.Connect();
        var data = strategy.GetData();
        strategy.ProcessData(data);
        strategy.Disconnect();
    }
}

class DatabaseStrategy : IDataAccessStrategy
{
    private List<Dictionary<string, object>> fakeDatabase;

    public void Connect()
    {
        Console.WriteLine("Connecting to database...");
        fakeDatabase = new List<Dictionary<string, object>>
        {
            new Dictionary<string, object> { { "Value", 10 } },
            new Dictionary<string, object> { { "Value", 20 } },
            new Dictionary<string, object> { { "Value", 30 } }
        };
    }

    public object GetData()
    {
        Console.WriteLine("Fetching data from database...");
        return fakeDatabase;
    }

    public void ProcessData(object data)
    {
        Console.WriteLine("Processing data from database...");
        var rows = data as List<Dictionary<string, object>>;
        int sum = rows.Sum(row => Convert.ToInt32(row["Value"]));
        Console.WriteLine($"Sum of 'Value' column: {sum}");
    }

    public void Disconnect()
    {
        Console.WriteLine("Disconnecting from database...");
    }
}

class XmlStrategy : IDataAccessStrategy
{
    private XDocument xmlDoc;

    public void Connect()
    {
        Console.WriteLine("Opening XML file...");
        string xmlContent = @"
        <root>
            <node name='short' />
            <node name='verylongnodenameindeed' />
            <node name='mediumname' />
        </root>";
        xmlDoc = XDocument.Parse(xmlContent);
    }

    public object GetData()
    {
        Console.WriteLine("Reading data from XML...");
        return xmlDoc;
    }

    public void ProcessData(object data)
    {
        Console.WriteLine("Processing XML data...");
        var doc = data as XDocument;
        var longest = doc.Descendants("node")
                         .Select(e => e.Attribute("name")?.Value)
                         .Where(name => name != null)
                         .OrderByDescending(name => name.Length)
                         .FirstOrDefault();
        Console.WriteLine($"Longest node name: {longest}");
    }

    public void Disconnect()
    {
        Console.WriteLine("Closing XML file...");
    }
}
