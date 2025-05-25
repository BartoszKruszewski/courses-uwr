using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;

[AttributeUsage(AttributeTargets.Constructor)]
public sealed class DependencyConstructorAttribute : Attribute { }

public class SimpleContainer
{
    private sealed class Registration
    {
        public Type ImplType { get; }
        public bool Singleton { get; }
        public object? Instance;

        public Registration(Type implType, bool singleton)
        {
            ImplType = implType;
            Singleton = singleton;
        }
    }

    private readonly Dictionary<Type, Registration> _registrations = new();

    public void RegisterType<T>(bool singleton = false) where T : class
        => RegisterType<T, T>(singleton);

    public void RegisterType<From, To>(bool singleton = false) where To : From
        => _registrations[typeof(From)] = new Registration(typeof(To), singleton);

    public void RegisterInstance<T>(T instance)
        => _registrations[typeof(T)] =
               new Registration(instance!.GetType(), singleton: true) { Instance = instance };

    public T Resolve<T>() => (T)Resolve(typeof(T), new HashSet<Type>());

    private object Resolve(Type service, HashSet<Type> callStack)
    {
        if (callStack.Contains(service))
            throw new InvalidOperationException($"Dependency cycle detected: {service.FullName}");

        if (_registrations.TryGetValue(service, out var reg))
        {
            if (reg.Singleton)
                return reg.Instance ??= Create(reg.ImplType, callStack);
            return Create(reg.ImplType, callStack);
        }

        if (!service.IsAbstract && !service.IsInterface)
            return Create(service, callStack);

        throw new InvalidOperationException($"Type {service.FullName} is not registered");
    }

    private object Create(Type implType, HashSet<Type> callStack)
    {
        callStack.Add(implType);
        try
        {
            var ctor = PickConstructor(implType);
            var args = ctor.GetParameters()
                           .Select(p => Resolve(p.ParameterType, callStack))
                           .ToArray();
            return ctor.Invoke(args)
                   ?? throw new InvalidOperationException($"Activator returned null for {implType.FullName}");
        }
        finally
        {
            callStack.Remove(implType);
        }
    }

    private static ConstructorInfo PickConstructor(Type t)
    {
        var marked = t.GetConstructors()
                      .Where(c => c.IsDefined(typeof(DependencyConstructorAttribute)))
                      .ToArray();
        if (marked.Length == 1)
            return marked[0];
        if (marked.Length > 1)
            throw new InvalidOperationException(
                $"Type {t.FullName} has multiple constructors marked [DependencyConstructor]");

        var ctorsByLen = t.GetConstructors()
                          .GroupBy(c => c.GetParameters().Length)
                          .OrderByDescending(g => g.Key)
                          .First();

        if (ctorsByLen.Count() > 1)
            throw new InvalidOperationException(
                $"Type {t.FullName} has several constructors with {ctorsByLen.Key} parameters; mark one with [DependencyConstructor]");

        return ctorsByLen.First();
    }
}
