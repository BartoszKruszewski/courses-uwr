#nullable enable

using System;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

void Run(Action action, [CallerArgumentExpression("action")] string? name = null)
{
    Console.Write($"{name}: ");
    try
    {
        action();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("OK");
    }
    catch
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("FAILED");
    }
    finally
    {
        Console.ResetColor();
    }
}

async Task RunAsync(Func<Task> action, [CallerArgumentExpression("action")] string? name = null)
{
    Console.Write($"{name}: ");
    try
    {
        await action();
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("OK");
    }
    catch
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("FAILED");
    }
    finally
    {
        Console.ResetColor();
    }
}
