#load "TestRunner.csx"
#r "nuget: MSTest.TestFramework, 3.1.0"
#r "nuget: MSTest.TestAdapter, 3.1.0"

using System;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;

public class Reusable
{
    public void DoWork()
    {
        Console.WriteLine("Working...");
    }
}

public sealed class ObjectPool
{
    private static readonly ObjectPool _instance = new ObjectPool(1);
    public static ObjectPool Instance => _instance;

    private readonly int _poolSize;
    private readonly List<Reusable> _pool = new List<Reusable>();
    private readonly List<Reusable> _acquired = new List<Reusable>();

    public ObjectPool(int poolSize)
    {
        if (poolSize <= 0)
        {
            throw new ArgumentException("Rozmiar puli musi być dodatni.");
        }
        _poolSize = poolSize;
    }

    public Reusable AcquireReusable()
    {
        if (_acquired.Count == _poolSize)
        {
            throw new ArgumentException("Brak wolnych zasobów w puli.");
        }

        if (_pool.Count == 0)
        {
            var reusable = new Reusable();
            _pool.Add(reusable);
        }

        var element = _pool[0];
        _pool.RemoveAt(0);
        _acquired.Add(element);
        return element;
    }

    public void ReleaseReusable(Reusable reusable)
    {
        if (!_acquired.Contains(reusable))
        {
            throw new ArgumentException("Zasób nie pochodzi z tej puli.");
        }

        _acquired.Remove(reusable);
        _pool.Add(reusable);
    }
}

public class BetterReusable
{
    private Reusable _reusable;
    private bool _isReleased = false;

    public BetterReusable()
    {
        _reusable = ObjectPool.Instance.AcquireReusable();
    }

    public void Release()
    {
        if (_isReleased)
        {
            throw new InvalidOperationException("Obiekt już został zwolniony.");
        }
        ObjectPool.Instance.ReleaseReusable(_reusable);
        _isReleased = true;
    }

    public void DoWork()
    {
        if (_isReleased)
        {
            throw new InvalidOperationException("Obiekt został już zwrócony do puli.");
        }
        _reusable.DoWork();
    }
}

public class BetterReusableForTest
{
    private readonly ObjectPool _pool;
    private Reusable _reusable;
    private bool _isReleased = false;

    public BetterReusableForTest(ObjectPool pool)
    {
        _pool = pool;
        _reusable = _pool.AcquireReusable();
    }

    public Reusable InnerReusable => _reusable;

    public void Release()
    {
        if (_isReleased)
        {
            throw new InvalidOperationException("Już zwolniony.");
        }
        _pool.ReleaseReusable(_reusable);
        _isReleased = true;
    }

    public void DoWork()
    {
        if (_isReleased)
        {
            throw new InvalidOperationException("Obiekt został zwolniony, nie można użyć.");
        }
        _reusable.DoWork();
    }
}

[TestClass]
public class Tests
{
    [TestMethod]
    public void InvalidSize()
    {
        Assert.ThrowsException<ArgumentException>(() =>
        {
            var pool = new ObjectPool(0);
        });
    }

    [TestMethod]
    public void ValidSize()
    {
        var tempPool = new ObjectPool(2);
        var br = new BetterReusableForTest(tempPool);
        Assert.IsNotNull(br);
    }

    [TestMethod]
    public void CapacityDepleted()
    {
        var tempPool = new ObjectPool(1);
        var br1 = new BetterReusableForTest(tempPool);

        Assert.ThrowsException<ArgumentException>(() =>
        {
            var br2 = new BetterReusableForTest(tempPool);
        });
    }

    [TestMethod]
    public void ReusedInstance()
    {
        var tempPool = new ObjectPool(1);
        var br1 = new BetterReusableForTest(tempPool);
        var firstReusable = br1.InnerReusable;
        br1.Release();

        var br2 = new BetterReusableForTest(tempPool);
        var secondReusable = br2.InnerReusable;

        Assert.AreEqual(firstReusable, secondReusable);
    }

    [TestMethod]
    public void ReleaseInvalidInstance()
    {
        var tempPool = new ObjectPool(1);
        var alienReusable = new Reusable();

        Assert.ThrowsException<ArgumentException>(() =>
        {
            tempPool.ReleaseReusable(alienReusable);
        });
    }

    [TestMethod]
    public void DoWorkAfterReleaseShouldThrow()
    {
        var br = new BetterReusable();
        br.Release();

        Assert.ThrowsException<InvalidOperationException>(() =>
        {
            br.DoWork();
        });
    }
}

var tests = new Tests();

Run(tests.InvalidSize);
Run(tests.ValidSize);
Run(tests.CapacityDepleted);
Run(tests.ReusedInstance);
Run(tests.ReleaseInvalidInstance);
Run(tests.DoWorkAfterReleaseShouldThrow);
