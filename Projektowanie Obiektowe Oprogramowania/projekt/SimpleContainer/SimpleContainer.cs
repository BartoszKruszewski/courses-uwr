using System;
using System.Collections.Generic;

public class SimpleContainer
{
    private class Registration
    {
        public Type ImplType;
        public bool Singleton;
        public object? Instance;

        public Registration(Type implType, bool singleton)
        {
            ImplType = implType;
            Singleton = singleton;
            Instance = null;
        }
    }

    private Dictionary<Type, Registration> registrations = new();

    public void RegisterType<T>(bool singleton) where T : class
        => RegisterType<T, T>(singleton);

    public void RegisterType<From, To>(bool singleton) where To : From
        => registrations[typeof(From)] = new Registration(typeof(To), singleton);

    public T Resolve<T>() => (T)Resolve(typeof(T));

    private object Resolve(Type t)
    {
        if (registrations.TryGetValue(t, out var reg))
        {
            if (reg.Singleton)
                return reg.Instance ??= Create(reg.ImplType);
            return Create(reg.ImplType);
        }

        if (t.IsInterface || t.IsAbstract)
            throw new InvalidOperationException($"Type {t.Name} not registered");

        return Create(t);
    }

    private object Create(Type t)
        => Activator.CreateInstance(t)
           ?? throw new InvalidOperationException($"Cannot create {t.Name}");
}