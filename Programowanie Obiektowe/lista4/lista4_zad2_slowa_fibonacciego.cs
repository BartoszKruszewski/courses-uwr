// Bartosz Kruszewski
// PO lista 4 zadanie 2
// 17-03-2023 Wersja 1.
// Program zawierajacy klasę FibonacciWords 
// oraz prezentuje jej działanie
// C# kompilator mono dla systemu Windows
// mcs lista4_zad2_slowa_fibonacciego.cs

using System;
using System.Collections;

class Program
{
    public static void Main()
    {
		//prezentacja klasy
        FibonacciWords fib = new FibonacciWords(6);
        foreach (string word in fib)
        {
            Console.WriteLine(word);
        }
    }
}

public class FibonacciWords : IEnumerable
{
	//słowa jakie będą zwracane
    private string[] words;

    public FibonacciWords(int size)
    {
		//utworzenie tablicy, która będzie przechowywać słowa
        this.words = new string[size];
		
		//przypisanie wartości pierwszym słwom
        this.words[0] = "b";
        this.words[1] = "a";
		
		//generowanie kolejnych słów na podstawie poprzednich
        for (int i = 2; i < size; i++)
        {
            this.words[i] = this.words[i - 1] + this.words[i - 2];
        }
    }

	//zwracanie numeratora
	IEnumerator IEnumerable.GetEnumerator()
    {
        return (IEnumerator)GetEnumerator();
    }

    public FibonacciEnum GetEnumerator()
    {
        return new FibonacciEnum(this.words);
    }
}

public class FibonacciEnum : IEnumerator
{
	//tablica ze słowami, które będą zwracane
    public string[] words;

	//pozycja początkowa
    int position = -1;

    public FibonacciEnum(string[] words)
    {
        this.words = words;
    }

    public bool MoveNext()
    {
        position++;
        return (position < words.Length);
    }

    public void Reset()
    {
        position = -1;
    }

    public object Current
    {
        get
        {
            return words[position];
        }
    }
}