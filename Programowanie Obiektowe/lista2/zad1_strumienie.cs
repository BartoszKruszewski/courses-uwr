// Bartosz Kruszewski
// PO lista 2 zadanie 1 
// Strumienie
// mcs lista2_zad1_strumienie.cs

using System;

class Program
{
    public static void Main()
    {
        //testy dla IntStream
        IntStream stream = new IntStream();
        Console.WriteLine("IntStream:");
        stream.Show(10);
        Console.WriteLine("reset");
        stream.Reset();
        stream.Show(10);
        Console.WriteLine(stream.Eos());
        
        //testy dla PrimeStream
        PrimeStream primeStream = new PrimeStream();
        Console.WriteLine("PrimeStream:");
        primeStream.Show(10);
        Console.WriteLine("reset");
        primeStream.Reset();
        primeStream.Show(10);
        Console.WriteLine(primeStream.Eos());

        //testy dla RandomStream
        RandomStream randomStream = new RandomStream();
        Console.WriteLine("RandomStream:");
        randomStream.Show(10);
        Console.WriteLine("reset");
        randomStream.Reset();
        randomStream.Show(10);
        Console.WriteLine(randomStream.Eos());

        //testy dla RandomWordStream
        RandomWordStream randomWordStream = new RandomWordStream();
        Console.WriteLine("RandomWordStream:");
        randomWordStream.Show(10);
        Console.WriteLine("reset");
        randomWordStream.Reset();
        randomWordStream.Show(10);
    }

    
}

class IntStream
{
    protected int ActualNumber = 0;
    protected bool IsEos = false;

    public virtual int Next()
    {
        //zapamietanie obecnej liczby, żeby ją później zwrócić
        int numberToReturn = ActualNumber;

        //sprawdzanie czy liczba mieści się w typie int
        if (ActualNumber < Int32.MaxValue)
        {
            ActualNumber += 1;
        }

        //ustawianie eos
        this.IsEos = ActualNumber == Int32.MaxValue;


        return numberToReturn;
    }

    public bool Eos()
    {
        return this.IsEos;
    }

    public virtual void Reset()
    {
        this.ActualNumber = 0;
    }
    
    //funkcja do wypisywania Next() kilka razy
    public void Show(int amount)
    {
        for (int i = 0; i < amount; i++)
        {
            Console.Write(this.Next());
            Console.Write(" ");
            
        }
    }
}

class PrimeStream : IntStream
{
    public PrimeStream()
    {
        this.ActualNumber = 2;
    }

    private bool IsPrime(int number)
    {
        int k = 2;
        while (k * k <= number)
        {
            if (number % k == 0)
            {
                return false;
            }

            k += 1;
        }

        return true;
    }

    public override int Next()
    {
        //zapamietanie obecnej liczby, żeby ją później zwrócić
        int numberToReturn = this.ActualNumber;

        //sprawdzanie kolejnych liczb czy są pierwsze
        while ((this.ActualNumber == numberToReturn ||
                !this.IsPrime(this.ActualNumber)) 
                && this.ActualNumber < Int32.MaxValue)
        {
            this.ActualNumber += 1;
        }

        //sprawdzanie czy liczba mieści się w typie int
        if (this.ActualNumber == Int32.MaxValue)
        {
            this.ActualNumber = numberToReturn;
            this.IsEos = true;
        }

        return numberToReturn;
    }

    public override void Reset()
    {
        //2 jest najmniejszą liczbą pierwszą 
        this.ActualNumber = 2;
    }
}

class RandomStream : IntStream
{
    //utworzenie obiektu do generowania liczb losowych
    private Random rnd = new Random();
    
    
    
    public RandomStream()
    {
        //losowanie liczby
        this.ActualNumber = Math.Abs(rnd.Next());
    }

    public override int Next()
    {
        //zapamietanie obecnej liczby, żeby ją później zwrócić
        int numberToReturn = this.ActualNumber;

        //losowanie nastepnej liczby
        this.ActualNumber = Math.Abs(rnd.Next());

        return numberToReturn;
    }

    public override void Reset()
    {
        this.ActualNumber = Math.Abs(rnd.Next());
    }
}

class RandomWordStream
{
    //utworzenie strumieni
    private PrimeStream primeStream = new PrimeStream();
    private RandomStream randomStream = new RandomStream();

    public string Next()
    {
        //wysolowanie długości wyrazu
        int len = primeStream.Next();

        //utworzenie pustegio wyrazu
        string word = "";

        //dodawanie losowych liczb naturalnych z przedziału od 0 do 9
        for (int i = 0; i < len; i++)
        {
            word += (randomStream.Next() % 10).ToString();
        }

        return word;
    }

    public void Reset()
    {
        //resetowanie strumienia z liczbami pierwszymi
        //resetowanie strumienia liczb losowych nie ma sensu
        primeStream.Reset();
    }
    
    //funkcja do wypisywania Next() kilka razy
    public void Show(int amount)
    {
        for (int i = 0; i < amount; i++)
        {
            Console.Write(this.Next());
            Console.Write(" ");
            
        }
    }
}