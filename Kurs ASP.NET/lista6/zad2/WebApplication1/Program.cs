using WebApplication1.Services;

var builder = WebApplication.CreateBuilder(args);

// Rejestracja us³ugi


//builder.Services.AddScoped<IDbConnectionService, DbConnectionService>();

// uzycie mocka zamiast bazy
builder.Services.AddScoped<IDbConnectionService, MockDbConnectionService>();

// Dodanie MVC
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Konfiguracja middleware
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
