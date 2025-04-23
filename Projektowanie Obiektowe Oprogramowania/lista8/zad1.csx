using System;
using System.IO;

var chain = new Classifier()
    .SetNext(new TypeHandler(MessageType.Praise, "Praise"))
    .SetNext(new TypeHandler(MessageType.Complaint, "Complaint"))
    .SetNext(new TypeHandler(MessageType.Order, "Order"))
    .SetNext(new TypeHandler(MessageType.Other, "Other"))
    .SetNext(new TypeHandler(MessageType.Invalid, "Invalid"))
    .SetNext(new ArchiveHandler());

var emails = new[]
{
    new Request("Thanks", "thank you for your help"),
    new Request("Problem", "I have a complaint about your service"),
    new Request("Buying", "I want to order a product"),
    new Request("Just Saying", "hi there"),
    new Request("Empty", "")
};

foreach (var email in emails)
    chain.Handle(email);

enum MessageType { Praise, Complaint, Order, Other, Invalid }

class Request
{
    public string Title, Content;
    public MessageType Type;
    public Request(string title, string content) => (Title, Content) = (title, content);
}

abstract class Handler
{
    protected Handler Next;
    public Handler SetNext(Handler next) { Next = next; return next; }
    public void Handle(Request req) { Process(req); Next?.Handle(req); }
    protected abstract void Process(Request req);
}

class Classifier : Handler
{
    protected override void Process(Request r)
    {
        if (string.IsNullOrWhiteSpace(r.Title) || string.IsNullOrWhiteSpace(r.Content) || r.Content.Length > 1000)
            r.Type = MessageType.Invalid;
        else if (r.Content.Contains("thank you")) r.Type = MessageType.Praise;
        else if (r.Content.Contains("complaint")) r.Type = MessageType.Complaint;
        else if (r.Content.Contains("order")) r.Type = MessageType.Order;
        else r.Type = MessageType.Other;
    }
}

class TypeHandler : Handler
{
    private MessageType _type;
    private string _label;
    public TypeHandler(MessageType type, string label) => (_type, _label) = (type, label);
    protected override void Process(Request r)
    {
        if (r.Type == _type) Console.WriteLine($"{_label}: {r.Title}");
    }
}

class ArchiveHandler : Handler
{
    protected override void Process(Request r)
    {
        File.AppendAllText("archive.txt", $"{DateTime.Now}: [{r.Type}] {r.Title} - {r.Content}\n");
    }
}
