var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => {
    string filePath = @"C:\temp\example.txt";
    string fileContent;

    try
    {
        using StreamReader sr = new StreamReader(filePath);
        fileContent = sr.ReadToEnd();
    }
    catch (Exception ex)
    {
        fileContent = ex.Message;
    }

    return Results.Text(fileContent);
});

app.Run();

