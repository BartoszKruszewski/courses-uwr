using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

var dbAccess = new DatabaseDataAccess();
dbAccess.Execute();

Console.WriteLine();

var xmlAccess = new XmlDataAccess();
xmlAccess.Execute();

abstract class DataAccessHandler
{
    public void Execute()
    {
        Connect();
        var data = GetData();
        ProcessData(data);
        Disconnect();
    }

    protected abstract void Connect();
    protected abstract object GetData();
    protected abstract void ProcessData(object data);
    protected abstract void Disconnect();
}

class DatabaseDataAccess : DataAccessHandler
{
    private List<Dictionary<string, object>> fakeDatabase;

    protected override void Connect()
    {
        Console.WriteLine("Connecting to database...");
        fakeDatabase = new List<Dictionary<string, object>>
        {
            new Dictionary<string, object> { { "Value", 10 } },
            new Dictionary<string, object> { { "Value", 20 } },
            new Dictionary<string, object> { { "Value", 30 } }
        };
    }

    protected override object GetData()
    {
        Console.WriteLine("Fetching data from database...");
        return fakeDatabase;
    }

    protected override void ProcessData(object data)
    {
        Console.WriteLine("Processing data from database...");
        var rows = data as List<Dictionary<string, object>>;
        int sum = rows.Sum(row => Convert.ToInt32(row["Value"]));
        Console.WriteLine($"Sum of 'Value' column: {sum}");
    }

    protected override void Disconnect()
    {
        Console.WriteLine("Disconnecting from database...");
    }
}

class XmlDataAccess : DataAccessHandler
{
    private XDocument xmlDoc;

    protected override void Connect()
    {
        Console.WriteLine("Opening XML file...");
        // Symulowany XML
        string xmlContent = @"
        <root>
            <node name='short' />
            <node name='verylongnodenameindeed' />
            <node name='mediumname' />
        </root>";
        xmlDoc = XDocument.Parse(xmlContent);
    }

    protected override object GetData()
    {
        Console.WriteLine("Reading data from XML...");
        return xmlDoc;
    }

    protected override void ProcessData(object data)
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

    protected override void Disconnect()
    {
        Console.WriteLine("Closing XML file...");
    }
}
