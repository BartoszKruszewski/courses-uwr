// dotnet script zad2.cs

var dataProvider = new ReportDataProvider();
var formatter = new ReportFormatter();
var printer = new ReportPrinter();

var data = dataProvider.GetData();
var formatted = formatter.FormatDocument(data);
printer.PrintReport(formatted);

public class ReportDataProvider
{
    public string GetData()
    {
        return "Jakieś dane";
    }
}

public class ReportFormatter
{
    public string FormatDocument(string data)
    {
        return "<html>" + data + "</html>";
    }
}

public class ReportPrinter
{
    public void PrintReport(string formattedData)
    {
        Console.WriteLine("Drukuję: " + formattedData);
    }
}