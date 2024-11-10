using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

// Rejestracja us�ugi w kontenerze DI
builder.Services.AddScoped<IDapperRepository, DapperRepository>();

var app = builder.Build();

// Endpoint GET z wstrzykni�ciem us�ugi IDapperRepository
app.MapGet("/", async (IDapperRepository repository) =>
{
    var data = await repository.GetDataAsync();
    return Results.Ok(data);
});

// Uruchomienie aplikacji
app.Run();


// Definiujemy interfejs us�ugi IDapperRepository
public interface IDapperRepository : IDisposable
{
    Task<string> GetDataAsync();
}

// Implementacja us�ugi DapperRepository
public class DapperRepository : IDapperRepository
{
    private bool _disposed = false;

    // Przyk�adowa metoda asynchroniczna zwracaj�ca dane
    public async Task<string> GetDataAsync()
    {
        await Task.Delay(100); // Symulacja op�nienia (np. zapytania do bazy danych)
        return "Hello from DapperRepository!";
    }

    // Implementacja IDisposable, aby prawid�owo zwalnia� zasoby
    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    protected virtual void Dispose(bool disposing)
    {
        if (_disposed) return;

        if (disposing)
        {
            // Zwolnienie zasob�w zarz�dzanych (je�li s� jakie�)
        }

        // Zwolnienie zasob�w niezarz�dzanych (je�li s� jakie�)

        _disposed = true;
    }

    ~DapperRepository()
    {
        Dispose(false);
    }
}


