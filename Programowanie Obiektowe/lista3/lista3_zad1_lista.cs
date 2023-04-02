// Bartosz Kruszewski
// PO lista 3 zadanie 1 lista
// Główny plik programu, pokazujący działanie klasy MyList
// C# kompilator mono dla systemu Windows
// mcs lista3_zad1_lista.cs -r:MyList.dll

// najpierw należy skompilowć plik MyList.cs 
// mcs -t:library MyList.cs

using System;

class Program
{
	public static void Main()
	{
		//tworzenie obiektu klasy
		MyList<int> list = new MyList<int>();
		
		//testy
		
		//czy lista jest pusta?
		Console.Write("Czy lista jest pusta? ");
		Console.WriteLine(list.IsEmpty());
		list.Show();
		Console.WriteLine();
		
		
		//dodawaie elementów "z przodu"
		Console.WriteLine("PushFront x10");
		for (int i = 0; i < 10; i++)
		{
			list.PushFront(i);
		}
		list.Show();
		Console.WriteLine();
		
		//dodawaie elementów "z tyłu"
		Console.WriteLine("PushBack x10");
		for (int i = 0; i < 10; i++)
		{
			list.PushBack(i);
		}
		list.Show();
		Console.WriteLine();
		
		//usuwanie ostatniego elementu
		Console.WriteLine("PopFront");
		Console.WriteLine(list.PopFront());
		list.Show();
		Console.WriteLine();
		
		//usuwanie ostatniego elementu
		Console.WriteLine("PopBack");
		Console.WriteLine(list.PopBack());
		list.Show();
		Console.WriteLine();
		
		//czy lista jest pusta?
		Console.Write("Czy lista jest pusta? ");
		Console.WriteLine(list.IsEmpty());
		list.Show();
	}
}