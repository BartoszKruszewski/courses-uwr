#r "System.IO"

using System;
using System.IO;

public interface ILogger
{
    void Log(string message);
}

public enum LogType { None, Console, File }

public class FileLogger : ILogger
{
    private readonly string _filePath;

    public FileLogger(string filePath)
    {
        _filePath = filePath;
    }

    public void Log(string message)
    {
        File.AppendAllText(_filePath, message + Environment.NewLine);
    }
}

public class ConsoleLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine(message);
    }
}

public class NullLogger : ILogger
{
    public void Log(string message) {}
}

public class LoggerFactory
{
    private static readonly LoggerFactory _instance = new LoggerFactory();
    public static LoggerFactory Instance => _instance;

    private LoggerFactory() {}

    public ILogger GetLogger(LogType logType, string parameters = null)
    {
        switch (logType)
        {
            case LogType.Console:
                return new ConsoleLogger();
            case LogType.File:
                return new FileLogger(parameters ?? "log.txt");
            case LogType.None:
            default:
                return new NullLogger();
        }
    }
}

LoggerFactory.Instance.GetLogger(LogType.Console).Log("To jest log na konsoli.");
LoggerFactory.Instance.GetLogger(LogType.File, "log.txt").Log("To jest log do pliku.");
LoggerFactory.Instance.GetLogger(LogType.None).Log("To się nigdzie nie zapisze.");
