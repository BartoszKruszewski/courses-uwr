public interface ICollection<T>
{
    // Właściwości „tylko do odczytu”
    int Count { get; }
    bool IsReadOnly { get; }

    // Metody odczytowe (co może być czasem użyteczne w scenariuszach „read-only”)
    bool Contains(T item);
    void CopyTo(T[] array, int arrayIndex);
    
    // Metody mutujące (dodawanie, usuwanie, czyszczenie)
    void Add(T item);
    bool Remove(T item);
    void Clear();
}

// Interfejs "tylko do odczytu" – nie wymusza żadnych metod modyfikujących.
public interface IReadOnlyCollection<T>
{
    int Count { get; }
    bool Contains(T item);
    void CopyTo(T[] array, int arrayIndex);
}

// Interfejs "mutowalny", rozszerzający funkcjonalność o dodawanie/usuwanie.
public interface IMutableCollection<T> : IReadOnlyCollection<T>
{
    void Add(T item);
    bool Remove(T item);
    void Clear();
}