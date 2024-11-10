using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Options;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

// Dodawanie plik�w konfiguracyjnych JSON i XML do konfiguracji aplikacji
builder.Configuration
    .AddJsonFile("appsettings2.json", optional: true, reloadOnChange: true)
    .AddXmlFile("appsettings.xml", optional: true, reloadOnChange: true);

// Rejestracja klasy `ConnectionSettings` do wstrzykiwania zale�no�ci poprzez IOptions
builder.Services.Configure<ConnectionSettings>(builder.Configuration.GetSection("ConnectionStrings"));

var app = builder.Build();

// Odczyt danych z konfiguracji za pomoc� IConfiguration
app.MapGet("/config", (IConfiguration config) =>
{
    // Odczyt danych za pomoc� indeksera
    string appTitle = config["AppTitle"];
    string version = config["Version"];
    string connectionString = config["ConnectionStrings:DefaultConnection"];

    return $"AppTitle: {appTitle}, Version: {version}, ConnectionString: {connectionString}";
});

// Odczyt danych z konfiguracji za pomoc� metody GetSection
app.MapGet("/section", (IConfiguration config) =>
{
    var section = config.GetSection("ConnectionStrings");
    string connectionString = section["DefaultConnection"];

    return $"Connection String from GetSection: {connectionString}";
});

// Odczyt danych za pomoc� wzorca IOptions
app.MapGet("/options", (IOptions<ConnectionSettings> options) =>
{
    string connectionString = options.Value.DefaultConnection;
    return $"Connection String from IOptions: {connectionString}";
});

// Start aplikacji
app.Run();

// Klasa modelu do przechowywania danych konfiguracyjnych
public class ConnectionSettings
{
    public string DefaultConnection { get; set; }
}
