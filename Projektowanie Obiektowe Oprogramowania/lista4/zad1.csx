#load "TestRunner.csx"
#r "nuget: MSTest.TestFramework, 3.1.0"
#r "nuget: MSTest.TestAdapter, 3.1.0"

using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Threading;

public sealed class ProcessSingleton
{
    private static readonly Lazy<ProcessSingleton> _instance =
        new Lazy<ProcessSingleton>(() => new ProcessSingleton());

    private ProcessSingleton() { }

    public static ProcessSingleton Instance => _instance.Value;

    public Guid Id { get; } = Guid.NewGuid();
}

public sealed class ThreadSingleton
{
    [ThreadStatic]
    private static ThreadSingleton _instance;

    private ThreadSingleton() { }

    public static ThreadSingleton Instance
    {
        get
        {
            if (_instance == null)
                _instance = new ThreadSingleton();
            return _instance;
        }
    }

    public Guid Id { get; } = Guid.NewGuid();
}

public sealed class TimedSingleton
{
    private static TimedSingleton _instance;
    private static DateTime _validUntil = DateTime.MinValue;

    private TimedSingleton() { }

    public static TimedSingleton Instance
    {
        get
        {
            if (_instance == null || DateTime.Now >= _validUntil)
            {
                _instance = new TimedSingleton();
                _validUntil = DateTime.Now.AddSeconds(5);
            }
            return _instance;
        }
    }

    public Guid Id { get; } = Guid.NewGuid();
}

[TestClass]
public class Tests
{
    [TestMethod]
    public void ProcessSingleton_SameInstance()
    {
        var a = ProcessSingleton.Instance;
        var b = ProcessSingleton.Instance;
        Assert.AreSame(a, b, "Different instances.");
    }

    [TestMethod]
    public void ProcessSingleton_SameId()
    {
        var a = ProcessSingleton.Instance.Id;
        var b = ProcessSingleton.Instance.Id;
        Assert.AreEqual(a, b, "Different Ids.");
    }

    [TestMethod]
    public void ProcessSingleton_SameInstanceAcrossThreads()
    {
        ProcessSingleton a = null, b = null;
        var t1 = new Thread(() => a = ProcessSingleton.Instance);
        var t2 = new Thread(() => b = ProcessSingleton.Instance);
        t1.Start(); t2.Start(); t1.Join(); t2.Join();
        Assert.AreSame(a, b, "Instances from threads are different.");
    }

    [TestMethod]
    public void ThreadSingleton_SameInSameThread()
    {
        var a = ThreadSingleton.Instance;
        var b = ThreadSingleton.Instance;
        Assert.AreSame(a, b, "Should be same in same thread.");
    }

    [TestMethod]
    public void ThreadSingleton_DifferentAcrossThreads()
    {
        ThreadSingleton a = null, b = null;
        var t1 = new Thread(() => a = ThreadSingleton.Instance);
        var t2 = new Thread(() => b = ThreadSingleton.Instance);
        t1.Start(); t2.Start(); t1.Join(); t2.Join();
        Assert.AreNotSame(a, b, "Should be different in different threads.");
    }

    [TestMethod]
    public void ThreadSingleton_DifferentIdsAcrossThreads()
    {
        Guid a = Guid.Empty, b = Guid.Empty;
        var t1 = new Thread(() => a = ThreadSingleton.Instance.Id);
        var t2 = new Thread(() => b = ThreadSingleton.Instance.Id);
        t1.Start(); t2.Start(); t1.Join(); t2.Join();
        Assert.AreNotEqual(a, b, "Ids should be different across threads.");
    }

    [TestMethod]
    public void TimedSingleton_SameWithin5Seconds()
    {
        var a = TimedSingleton.Instance;
        Thread.Sleep(1000);
        var b = TimedSingleton.Instance;
        Assert.AreSame(a, b, "Should be same within 5 seconds.");
    }

    [TestMethod]
    public void TimedSingleton_DifferentAfter5Seconds()
    {
        var a = TimedSingleton.Instance;
        Thread.Sleep(6000);
        var b = TimedSingleton.Instance;
        Assert.AreNotSame(a, b, "Should be different after 5 seconds.");
    }

    [TestMethod]
    public void TimedSingleton_DifferentIdAfter5Seconds()
    {
        var a = TimedSingleton.Instance.Id;
        Thread.Sleep(6000);
        var b = TimedSingleton.Instance.Id;
        Assert.AreNotEqual(a, b, "Id should be different after 5 seconds.");
    }
}

var tests = new Tests();

Run(tests.ProcessSingleton_SameInstance);
Run(tests.ProcessSingleton_SameId);
Run(tests.ProcessSingleton_SameInstanceAcrossThreads);
Run(tests.ThreadSingleton_SameInSameThread);
Run(tests.ThreadSingleton_DifferentAcrossThreads);
Run(tests.ThreadSingleton_DifferentIdsAcrossThreads);
Run(tests.TimedSingleton_SameWithin5Seconds);
Run(tests.TimedSingleton_DifferentAfter5Seconds);
Run(tests.TimedSingleton_DifferentIdAfter5Seconds);
