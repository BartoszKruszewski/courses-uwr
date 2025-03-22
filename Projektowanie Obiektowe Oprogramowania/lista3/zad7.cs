// dotnet script zad7.cs

IReportDataProvider dataProvider = new ReportDataProvider();
IReportFormatter formatter = new ReportFormatter();
IReportPrinter printer = new ReportPrinter();

var composer = new ReportComposer(dataProvider, formatter, printer);
composer.ComposeAndPrintReport();

public interface IReportDataProvider
{
    string GetData();
}

public interface IReportFormatter
{
    string FormatDocument(string data);
}

public interface IReportPrinter
{
    void PrintReport(string formattedData);
}


public class ReportDataProvider : IReportDataProvider
{
    public string GetData()
    {
        return "Jakieś dane";
    }
}

public class ReportFormatter : IReportFormatter
{
    public string FormatDocument(string data)
    {
        return "<html>" + data + "</html>";
    }
}

public class ReportPrinter : IReportPrinter
{
    public void PrintReport(string formattedData)
    {
        Console.WriteLine("Drukuję raport:" + formattedData);
    }
}

public class ReportComposer
{
    private readonly IReportDataProvider _dataProvider;
    private readonly IReportFormatter _formatter;
    private readonly IReportPrinter _printer;

    public ReportComposer(
        IReportDataProvider dataProvider,
        IReportFormatter formatter,
        IReportPrinter printer)
    {
        _dataProvider = dataProvider;
        _formatter = formatter;
        _printer = printer;
    }

    public void ComposeAndPrintReport()
    {
        string data = _dataProvider.GetData();
        string formattedData = _formatter.FormatDocument(data);
        _printer.PrintReport(formattedData);
    }
}
