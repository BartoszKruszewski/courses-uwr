// Bartosz Kruszewski
// PO lista 4 zadanie 1 
// 17-03-2023 Wersja 1.
// Program zawierajacy klasy Vector i MyList, interfejs ListCollection
// oraz prezentuje ich działanie
// C# kompilator mono dla systemu Windows
// mcs lista4_zad1_interfejs.cs

using System;
using System.Collections;

//główny program prezetujący działanie klas Vector i MyList
class Program
{
    public static void Main()
    {
        //prezentacja klasy Vector
        Vector v = new Vector(4);
        v.SetValues(new object[] {1.0f, 2.0f, 3.0f, 4.0f});
        Console.WriteLine("Wartości wektora v:");
        foreach (float value in v)
        {
            Console.WriteLine(value);
        }
        Console.WriteLine("Metoda ToString() wektora v zwraca:");
        Console.WriteLine(v.ToString());
        Console.WriteLine("Właściwość Length wektora v zwraca:");
        Console.WriteLine(v.Length);
        Console.WriteLine("Dostęp indeksowy v[2] zwraca:");
        Console.WriteLine(v[2]);
		
		//prezentacja klasy MyList
		MyList<float> l = new MyList<float>();
		l.PushFront(1.0f);
		l.PushFront(3.0f);
		l.SetValues(new object[] {10.0f, 5.0f, 3.0f, 4.0f});
		l.Show();
		
    }
}

//interfejs ListCollection 
public interface ListCollection
{
	//metoda Show(), która wyświetla kolekcję
    void Show();
	
	//metoda SetValues(), która ustawia wartości elementów kolekcji
    void SetValues(object[] values);
}

public class MyList<T> : ListCollection
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

    public void SetValues(object[] values)
    {
		//ustawia wartości elementom, które są na liście
		//dodatkowo podane wartości jako argumnety są ignorowane
		
        //aktualny element, którego wartość będziemy zmieniać
        ListItem<T> actualItem = head;

        //licznik, który element jest aktualnie zmieniany
        int i = 0;

        //zmiana wartości elementów, aż do końca listy
        while (actualItem != null)
        {
            //ustawienie wartości aktualnego elementu
            actualItem.value = (T)values[i];

            //ustawianie aktualnego elementu listy jako jego następnik
            actualItem = actualItem.next;

            //zwiększenie licznika o 1
            i++;
        }
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

public class Vector : ListCollection, IEnumerable
{
    //tablica wartości wektora
    private float[] values;

    //wymiar wektora
    private int dim;

    public Vector(int n)
    {
        //sprawdzanie czy wymiar wektora jest ujemny
        if (n < 0)
        {
            throw new ArgumentException("Wymiar wektora nie może ujemny!");
        }

        //ustawianie wektora oraz wielkości tablicy wartości
        this.dim = n;
        this.values = new float[n];
    }


    public void SetValues(object[] values)
    {
        //sprawdzanie czy podano poprawną ilość wartości
        if (values.Length != this.values.Length)
        {
            throw new ArgumentException(
                "Nieprawidłowa wielkość tablicy wartości!");
        }

        //ustawianie wartości wektora za pomocą zewnętrznej tablicy
        for (int i = 0; i < this.dim; i++)
        {
            this.values[i] = (float)values[i];
        }
    }

    public void Show()
    {
        //wypisywanie wartości wektora
        Console.Write("[");
        for (int i = 0; i < this.dim; i++)
        {
            Console.Write(this.values[i]);
            if (i != this.dim - 1)
            {
                Console.Write(", ");
            }
        }

        Console.WriteLine("]");
    }

    public static Vector operator +(Vector a, Vector b)
    {
        //sprawdzanie czy wektory mają taki sam wymiar
        if (a.dim != b.dim)
        {
            throw new ArgumentException(
                "Nie można dodać wektorów o różnych wymiarach!");
        }

        //tworzenie nowego wektora
        Vector newVector = new Vector(a.dim);

        for (int i = 0; i < a.dim; i++)
        {
            //dodawanie wartości dla każdej współrzędnej
            newVector.values[i] = a.values[i] + b.values[i];
        }

        return newVector;
    }

    public static float operator *(Vector a, Vector b)
    {
        //sprawdzanie czy wektory mają taki sam wymiar
        if (a.dim != b.dim)
        {
            throw new ArgumentException(
                "Nie można pomnożyć wektorów o różnych wymiarach!");
        }

        //suma, którą będziemy zwracać
        float result = 0;

        for (int i = 0; i < a.dim; i++)
        {
            //dodawanie iloczynu wartości dla każdej współrzędnej
            result += a.values[i] * b.values[i];
        }

        return result;
    }

    public static Vector operator *(Vector a, float s)
    {
        //tworzenie nowego wektora
        Vector newVector = new Vector(a.dim);

        for (int i = 0; i < a.dim; i++)
        {
            //mnożenie przez skalar
            newVector.values[i] = a.values[i] * s;
        }

        return newVector;
    }

    public override string ToString()
    {
        //utworzenie stringa, którego będziemy konkatenować
        string result = "[";
        
        for (int i = 0;i < this.dim; i++)
        {
            //dodawanie kolejnych wartości
            result += values[i].ToString();
            
            //dodawanie odstępu pomiędzy wartościami,
            //jeżeli wartość nie jest ostatnia
            if (i != this.dim - 1)
            {
                result += ", ";
            }
        }
        
        //dopisanie klamerki (w celach estetycznych)
        result += "]";

        return result;
    }

    //funkcja pozawalająca na używanie dostępu indeksowanego
    public float this[int index]
    {
        get
        {
            return this.values[index];
        }
    }
    
    public float Length
    {
        get
        {
            //zwracanie długości wektora,
            //liczy to zrobiona na potrzeby poprzedniego zadania
            //funkcja norma()
            return this.norma();
        }
    }

    private float norma()
    {
        //suma, którą będziemy zwracać
        float result = 0;

        for (int i = 0; i < this.dim; i++)
        {
            result += this.values[i] * this.values[i];
        }

        //wyciągnięcie pierwiastka
        return (float)Math.Sqrt(result);
    }
	
	IEnumerator IEnumerable.GetEnumerator()
    {
        return (IEnumerator)GetEnumerator();
    }

	
    //zwracanie numeratora
    public IEnumerator GetEnumerator()
    {
        return new VectorEnum(this.values);
    }
}
//klasa numeratiora dla klasy Vector
class VectorEnum : IEnumerator
{
    //wartosci do zwracania
    private float[] values;
    
    //pozycja
    private int position = -1;
    public VectorEnum(float[] values)
    {
        this.values = values;
    }
    
    public bool MoveNext()
    {
        position++;
        return position < values.Length;
    }

    public void Reset()
    {
        position = -1;
    }

    public object Current
    {
        get
        {
            return values[position];
        }
    }
    
}