using System;
using System.Threading;

public interface IWeatherService
{
    string GetWeather();
}

public class WeatherService : IWeatherService
{
    private readonly Random _rand = new Random();
    public string GetWeather()
    {
        if (_rand.NextDouble() < 0.5)
            throw new Exception("Weather API failed!");
        return "Sunny";
    }
}

public class RetryWeatherProxy : IWeatherService
{
    private readonly IWeatherService _realService;
    private readonly int _maxRetries;

    public RetryWeatherProxy(IWeatherService realService, int maxRetries = 3)
    {
        _realService = realService;
        _maxRetries = maxRetries;
    }

    public string GetWeather()
    {
        int attempts = 0;
        while (true)
        {
            try
            {
                Console.WriteLine($"[RetryProxy] Attempt {attempts + 1}");
                return _realService.GetWeather();
            }
            catch (Exception ex)
            {
                attempts++;
                Console.WriteLine($"[RetryProxy] Failed: {ex.Message}");
                if (attempts >= _maxRetries)
                    throw;
                Thread.Sleep(300);
            }
        }
    }
}

public class FallbackWeatherProxy : IWeatherService
{
    private readonly IWeatherService _realService;
    private readonly string _fallbackValue;

    public FallbackWeatherProxy(IWeatherService realService, string fallbackValue = "Unknown")
    {
        _realService = realService;
        _fallbackValue = fallbackValue;
    }

    public string GetWeather()
    {
        try
        {
            return _realService.GetWeather();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"[FallbackProxy] Error: {ex.Message}");
            Console.WriteLine($"[FallbackProxy] Returning fallback value: {_fallbackValue}");
            return _fallbackValue;
        }
    }
}

Console.WriteLine("== RETRY PROXY ==");
var retryService = new RetryWeatherProxy(new WeatherService());
try
{
    string weather1 = retryService.GetWeather();
    Console.WriteLine($"[RetryClient] Weather: {weather1}");
}
catch (Exception ex)
{
    Console.WriteLine($"[RetryClient] All attempts failed: {ex.Message}");
}

Console.WriteLine();

Console.WriteLine("== FALLBACK PROXY ==");
var fallbackService = new FallbackWeatherProxy(new WeatherService(), "Rainy");
string weather2 = fallbackService.GetWeather();
Console.WriteLine($"[FallbackClient] Weather: {weather2}");
