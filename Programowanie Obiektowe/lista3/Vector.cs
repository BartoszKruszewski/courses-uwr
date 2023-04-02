// Bartosz Kruszewski
// PO lista 3 zadanie 4 Wektor
// Biblioteka klas zawierająca klasę Vector
// C# kompilator mono dla systemu Windows
// mcs -t:library Vector.cs

using System;

public class Vector
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

	
    public void SetValues(float[] values)
    {
		//sprawdzanie czy podano poprawną ilość wartości
		if (values.Length != this.values.Length)
        {
            throw new ArgumentException("Nieprawidłowa wielkość tablicy wartości!");
        }
		
		//ustawianie wartości wektora za pomocą zewnętrznej tablicy
        this.values = values;
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
            throw new ArgumentException("Nie można dodać wektorów o różnych wymiarach!");
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
            throw new ArgumentException("Nie można pomnożyć wektorów o różnych wymiarach!");
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

    public float norma()
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
}