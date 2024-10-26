using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Map("/", async (HttpContext context) =>
{
    var fullUrl = $"{context.Request.Scheme}://{context.Request.Host}{context.Request.Path}{context.Request.QueryString}";
    var headers = context.Request.Headers.ToDictionary(h => h.Key, h => h.Value.ToString());
    var method = context.Request.Method;
    string content = string.Empty;
    if (method == "POST" && context.Request.ContentLength > 0)
    {
        using var reader = new System.IO.StreamReader(context.Request.Body);
        content = await reader.ReadToEndAsync();
    }

    var response = new
    {
        FullUrl = fullUrl,
        Headers = headers,
        Method = method,
        Content = string.IsNullOrEmpty(content) ? "Brak treœci" : content
    };

    context.Response.ContentType = "application/json";
    await context.Response.WriteAsJsonAsync(response);
});

app.Run();
