using System;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

// Rejestracja us³ugi w kontenerze DI
builder.Services.AddScoped<IDapperRepository, DapperRepository>();

var app = builder.Build();

// Endpoint GET z wstrzykniêciem us³ugi IDapperRepository
app.MapGet("/", async (IDapperRepository repository) =>
{
    var data = await repository.GetDataAsync();
    return Results.Ok(data);
});

// Uruchomienie aplikacji
app.Run();


// Definiujemy interfejs us³ugi IDapperRepository
public interface IDapperRepository : IDisposable
{
    Task<string> GetDataAsync();
}

// Implementacja us³ugi DapperRepository
public class DapperRepository : IDapperRepository
{
    private bool _disposed = false;

    // Przyk³adowa metoda asynchroniczna zwracaj¹ca dane
    public async Task<string> GetDataAsync()
    {
        await Task.Delay(100); // Symulacja opóŸnienia (np. zapytania do bazy danych)
        return "Hello from DapperRepository!";
    }

    // Implementacja IDisposable, aby prawid³owo zwalniaæ zasoby
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
            // Zwolnienie zasobów zarz¹dzanych (jeœli s¹ jakieœ)
        }

        // Zwolnienie zasobów niezarz¹dzanych (jeœli s¹ jakieœ)

        _disposed = true;
    }

    ~DapperRepository()
    {
        Dispose(false);
    }
}


