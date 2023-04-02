// Bartosz Kruszewski
// PO lista 3 zadanie 1 lista
// Główny plik programu, pokazujący działanie klasy Vector
// C# kompilator mono dla systemu Windows
// mcs lista3_zad4_wektor.cs -r:Vector.dll

// najpierw należy skompilowć plik Vector.cs 
// mcs -t:library Vector.cs

using System;

class Program
{
    public static void Main()
    {
		//testy
		
		//tworzenie nowych wektorów
        Vector a = new Vector(3);
        Vector b = new Vector(3);
		
		//przypisywanie wartości 
        a.SetValues(new float[] { 1.2f, 2.2f, 3.7f });
        b.SetValues(new float[] { 3.5f, 3.1f, 21.4f });
		Console.WriteLine("Wektory:");
		a.Show();
		b.Show();
		Console.WriteLine();
		
		//dodawanie
		Console.WriteLine("Dodawanie:");
        (a + b).Show();
		Console.WriteLine();
		
		//iloczyn skalarany
		Console.WriteLine("Iloczyn Skalarny:");
        Console.WriteLine(a * b);
		Console.WriteLine();
		
		//mnożenie przez skalar
		Console.WriteLine("Mnożenie przez skalar 5.2:");
		Vector x = a * 5.2f;
        x.Show();
		Vector y = b * 5.2f;
        y.Show();
		Console.WriteLine();
		
		//długość wektora
		Console.WriteLine("Długości:");
        Console.WriteLine(a.norma());
        Console.WriteLine(b.norma());
    }
}

