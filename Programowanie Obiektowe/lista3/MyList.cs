// Bartosz Kruszewski
// PO lista 3 zadanie 1 lista
// Biblioteka klas zawierająca klasy MyList oraz ListItem
// C# kompilator mono dla systemu Windows
// mcs -t:library MyList.cs

using System;

public class MyList<T>
{
	//pierwszy element listy
	private ListItem<T> head;
	//ostatni element listy
	private ListItem<T> last;

	public MyList()
	{
		//lista jest pusta po utworzeniu nowego obiektu
		this.head = null;
		this.last = null;
	}

	public void PushFront(T elem)
	{
		//tworzenie obiektu nowego elementu listy 
		ListItem<T> newItem = new ListItem<T>(elem);
		//jeżeli lista jest pusta to zostaje on jednocześnie
		//pierwszym i ostatnim obiektem
		if (this.IsEmpty())
		{
			head = newItem;
			last = head;
		}
		//w przeciwnym przypadku przypisujemy go do obecnie
		//ostatniego obiektu
		else
		{
			last.next = newItem;
			last.next.pre = last;
			last = newItem;
		}
	}
	
	public void PushBack(T elem)
	{
		//analogicznie jak PushFront
		ListItem<T> newItem = new ListItem<T>(elem);
		if (this.IsEmpty())
		{
			head = newItem;
			last = head;
		}
		else
		{
			newItem.next = head;
			head.pre = newItem;
			head = newItem;
		}
	}
	
	public T PopFront()
	{
		//zapamiętanie wartości elementu z końca listy
		T popValue = last.value;
		//ustawienie przedostatniego elemetu jako ostatni
		last = last.pre;
		last.next = null;
		return popValue;
	}
	
	public T PopBack()
	{
		//zapamiętanie wartości elementu z początku listy
		T popValue = head.value;
		//ustawienie drugiego elemetu jako pierwszy
		head = head.next;
		return popValue;
	}
	
	public bool IsEmpty()
	{
		//jeżeli pierwszy element nie jest przypisany
		//do żadnego elementu listy to lista jest pusta
		return head == null;
	}

	public void Show()
	{
		//aktualny element, który będzie wypisywany
		ListItem<T> actualItem = head;
		
		//wypisywanie elementu, aż do końca listy
		Console.Write("[");
		while (actualItem != null)
		{
			Console.Write(actualItem.value);
			
			//sprawdzanie czy element jest ostatni
			if (actualItem.next != null)
			{
				Console.Write(", ");
			}
			
			//ustawianie aktualnego elementu listy jako jego następnik
			actualItem = actualItem.next;
		}
		Console.WriteLine("]");
	}
}

class ListItem<T>
{
	//wartość elementu
	public T value;
	
	//następny element listy
	public ListItem<T> next;
	
	//poprzedni element listy
	public ListItem<T> pre;
	
	public ListItem(T elem)
	{
		value = elem;
	}
}