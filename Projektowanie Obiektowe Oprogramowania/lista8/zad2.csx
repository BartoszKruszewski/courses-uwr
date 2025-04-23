#r "System.Net.Http"
using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Threading;
using System.Collections.Concurrent;

var handler = new FileHandler();
var invoker = new CommandQueue();
invoker.Start();

invoker.Enqueue(new CreateRandom(handler, "random.bin", 512));
invoker.Enqueue(new CopyFile(handler, "random.bin", "copy.bin"));
invoker.Enqueue(new HttpDownload(handler, "https://example.com", "page.html"));

Thread.Sleep(3000);
invoker.Stop();

public interface ICommand
{
    void Execute();
}

public class FileHandler
{
    public void DownloadFtp(string url, string path)
    {
        new WebClient().DownloadFile(url, path);
        Console.WriteLine($"[FTP] Downloaded {url} → {path}");
    }

    public void DownloadHttp(string url, string path)
    {
        var data = new HttpClient().GetByteArrayAsync(url).Result;
        File.WriteAllBytes(path, data);
        Console.WriteLine($"[HTTP] Downloaded {url} → {path}");
    }

    public void CreateRandomFile(string path, int size)
    {
        var data = new byte[size];
        new Random().NextBytes(data);
        File.WriteAllBytes(path, data);
        Console.WriteLine($"[RANDOM] Created {path} ({size}B)");
    }

    public void CopyFile(string from, string to)
    {
        File.Copy(from, to, true);
        Console.WriteLine($"[COPY] {from} → {to}");
    }
}

public class FtpDownload : ICommand
{
    string url, path; FileHandler h;
    public FtpDownload(FileHandler h, string url, string path) { this.h = h; this.url = url; this.path = path; }
    public void Execute() => h.DownloadFtp(url, path);
}

public class HttpDownload : ICommand
{
    string url, path; FileHandler h;
    public HttpDownload(FileHandler h, string url, string path) { this.h = h; this.url = url; this.path = path; }
    public void Execute() => h.DownloadHttp(url, path);
}

public class CreateRandom : ICommand
{
    string path; int size; FileHandler h;
    public CreateRandom(FileHandler h, string path, int size) { this.h = h; this.path = path; this.size = size; }
    public void Execute() => h.CreateRandomFile(path, size);
}

public class CopyFile : ICommand
{
    string from, to; FileHandler h;
    public CopyFile(FileHandler h, string from, string to) { this.h = h; this.from = from; this.to = to; }
    public void Execute() => h.CopyFile(from, to);
}

public class CommandQueue
{
    BlockingCollection<ICommand> queue = new();

    public void Enqueue(ICommand cmd) => queue.Add(cmd);

    public void Start(int workers = 2)
    {
        for (int i = 0; i < workers; i++)
        {
            new Thread(() =>
            {
                foreach (var cmd in queue.GetConsumingEnumerable())
                {
                    try { cmd.Execute(); } catch (Exception e) { Console.WriteLine($"[ERROR] {e.Message}"); }
                }
            }) { IsBackground = true }.Start();
        }
    }

    public void Stop() => queue.CompleteAdding();
}


