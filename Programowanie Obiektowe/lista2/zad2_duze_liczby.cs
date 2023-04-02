// Bartosz Kruszewski
// PO lista 2 zadanie 3 
// Klasa przechowująca duże liczby
// mcs lista2_zad3_duze_liczby.cs

using System;

class Program
{
    public static void Main()
    {
        //testy
        Console.WriteLine();
        Console.WriteLine("=-----=-----=-----=-----=-----=-----= " +
                          "Testy =-----=-----=-----=-----=-----=-----=");
        Console.WriteLine();
        Console.WriteLine("| Dane 1 | Dane 2 | Wynik int + " +
                          "| Wynik BigNum + | Wynik int - | Wynik BigNum - |");
        int[,] tests =
        {
            { 0, 0 },
            { 1, 1 },
            { 100, 100 },
            { 10, 10 },
            { 9999, 9999 },
            { 9999, 999 },
            { 999, 0 },
            { 756, 723 },
            { 10, 10 },
            { 10, 45 },
            { -82, 10 },
            { 15, -10 },
            { -10, -10 },
            { -10, 0 },
            { 0, -999 },
            { -999, 999 },
        };
        
        //wyświetlanie testów
        for (int i = 0; i < tests.Length / 2; i++)
        {
            BigNum a = new BigNum(tests[i, 0]);
            BigNum b = new BigNum(tests[i, 1]);
            String FirstNumber = tests[i, 0].ToString();
            String SecondNumber = tests[i, 1].ToString();
            String IntSum = (tests[i, 0] + tests[i, 1]).ToString();
            String BigNumSum = (a + b).GetValue();
            String IntSub = (tests[i, 0] - tests[i, 1]).ToString();
            String BigNumSub = (a - b).GetValue();

            Console.WriteLine(
                "| " + FirstNumber + GetSpaces(7 - FirstNumber.Length) + "| " +
                SecondNumber + GetSpaces(7 - SecondNumber.Length) + "| " +
                IntSum + GetSpaces(12 - IntSum.Length) + "| " +
                BigNumSum + GetSpaces(15 - BigNumSum.Length) + "| " +
                IntSub + GetSpaces(12 - IntSub.Length) + "| " +
                BigNumSub + GetSpaces(15 - BigNumSub.Length) + "|");
            
        }
        
        Console.WriteLine();
        
        //test dla bardzo dużych liczb
        BigNum bigA = new BigNum(Int32.MaxValue);
        for (int i = 0; i < 100; i++)
        {
            bigA = bigA + bigA;
        }
        Console.WriteLine("Maksymalna wartość dla typu " +
                          "int dodana do siebie wielokrotnie:");
        bigA.Show();
        BigNum bigB = new BigNum(Int32.MaxValue);
        for (int i = 0; i < 100; i++)
        {
            bigB = bigB - bigA;
        }
        Console.WriteLine("Maksymalna wartość dla typu " +
                          "int odjęta od liczby wielokrotnie:");
        bigB.Show();
        
    }

    //funkcja zwracająca zadaną ilość spacji
    public static string GetSpaces(int amount)
    {
        string spaces = "";
        for (int i = 0; i < amount; i++)
        {
            spaces += " ";
        }

        return spaces;
    }
}


class BigNum
{
    //zmienna przechowująca znak
    private bool negative;

    //zmienna przechowująca wartość bezwzględną liczby
    private string value;

    public BigNum(int value)
    {
        //uwzględnianie znaku
        this.negative = value < 0;

        //zamiana wartości typu int na string
        this.value = Math.Abs(value).ToString();
    }

    public string GetValue()
    {
        if (this.negative && this.value != "0")
        {
            //z minusem dla liczb ujemnych
            return "-" + this.value;
        }
        else
        {
            //bez minusa dla reszty liczb
            return this.value;
        }
    }

    public void Show()
    {
        //skorzystanie z funkcji GetValue()
        Console.WriteLine(this.GetValue());
    }

    public static BigNum operator +(BigNum a, BigNum b)
    {
        //sprawdzanie czy można uprościć dodawanie

        //dla dwóch liczb ujemnych
        if (a.negative && b.negative)
        {
            bool IsANegative = a.negative;
            bool IsBNegative = b.negative;
            a.negative = false;
            b.negative = false;
            BigNum absResult = a + b;
            a.negative = IsANegative;
            b.negative = IsBNegative;
            absResult.negative = true;
            return absResult;
        }
        //dla jednej liczby ujemnej
        else if (b.negative)
        {
            bool IsANegative = a.negative;
            bool IsBNegative = b.negative;
            a.negative = false;
            b.negative = false;
            BigNum absResult = a - b;
            a.negative = IsANegative;
            b.negative = IsBNegative;
            return absResult;
        }
        else if (a.negative)
        {
            bool IsANegative = a.negative;
            bool IsBNegative = b.negative;
            a.negative = false;
            b.negative = false;
            BigNum absResult = b - a;
            a.negative = IsANegative;
            b.negative = IsBNegative;
            return absResult;
        }
        else
        {
            //algorytm dodawania pisemnego dla dwóch dodatnich liczb

            //nowy obiekt dużej liczby, który będziemy zwracać
            BigNum result = new BigNum(0);

            //wartość jaką będziemy przypisywać nowemu obiektowi
            string newValue = "";

            //zmienne pomocnicze przy dodawaniu pisemnym
            int aDigit, bDigit, pDigit = 0, sum;

            //sprawdzanie, który składnik sumy jest dłuższy w zapisie
            int mLength = Math.Max(a.value.Length, b.value.Length);
            string aValue = a.value;
            string bValue = b.value;

            //dopisywanie brakujących zer do dodawania
            for (int i = 0; i < mLength - a.value.Length; i++)
            {
                aValue = "0" + aValue;
            }

            for (int i = 0; i < mLength - b.value.Length; i++)
            {
                bValue = "0" + bValue;
            }

            //główna pętla dodawania
            for (int i = mLength - 1; i >= 0; i--)
            {
                //zamiana wartości z typu string do int
                aDigit = Convert.ToInt32(aValue[i].ToString());
                bDigit = Convert.ToInt32(bValue[i].ToString());

                //sumowanie
                sum = aDigit + bDigit + pDigit;

                //dopisywanie wyniku z "jednej linii" do całości
                newValue = (sum % 10) + newValue;

                //"przerzucanie reszty wartości do następnej linijki"
                pDigit = sum / 10;
            }

            //dopisywanie reszty z przodu, jeżeli jakaś została
            if (pDigit != 0)
            {
                newValue = pDigit + newValue;
            }

            //przypisanie obliczonej wartości do wcześniej utworzonego obiektu
            result.value = newValue;

            //zwracenie obiektu
            return result;
        }
    }

    public static BigNum operator -(BigNum a, BigNum b)
    {
        //sprawdzanie czy można uprościć odjemowanie

        //dla dwóch liczb ujemnych
        if (a.negative && b.negative)
        { 
            bool IsANegative = a.negative;
            bool IsBNegative = b.negative;
            a.negative = false;
            b.negative = false;
            BigNum absResult = b - a;
            
            a.negative = IsANegative;
            b.negative = IsBNegative;
            absResult.negative = true;
            return absResult;
        }

        //dla jednej liczby ujemnej
        else if (b.negative)
        {
            bool IsANegative = a.negative;
            bool IsBNegative = b.negative;
            a.negative = false;
            b.negative = false;
            BigNum absResult = a + b;
            a.negative = IsANegative;
            b.negative = IsBNegative;
            return absResult;
        }
        else if (a.negative)
        {
            bool IsANegative = a.negative;
            bool IsBNegative = b.negative;
            a.negative = false;
            b.negative = false;
            BigNum absResult = a + b;
            a.negative = IsANegative;
            b.negative = IsBNegative;
            absResult.negative = true;
            return absResult;
        }
        
        //sprawdzanie czy druga liczba jest większa
        //w celu zamiany ich miejscami oraz zamiany znaku
        else if (a.value.Length < b.value.Length || 
                 (a.value.Length == b.value.Length 
                  && a.value[0] < b.value[0]))
        {
            BigNum absResult = b - a;
            absResult.negative = true;
            return absResult;
        }
        else
        {
            //algorytm odejmowania pisemnego dla dwóch dodatnich liczb
            //bardzo podobny do dodawania

            //nowy obiekt dużej liczby, który będziemy zwracać
            BigNum result = new BigNum(0);

            //wartość jaką będziemy przypisywać nowemu obiektowi
            string newValue = "";

            //zmienne pomocnicze przy dodawaniu pisemnym
            int aDigit, bDigit, pDigit = 0, sum;

            //sprawdzanie, który składnik sumy jest dłuższy w zapisie
            int mLength = Math.Max(a.value.Length, b.value.Length);
            string aValue = a.value;
            string bValue = b.value;

            //dopisywanie brakujących zer do odejmowania
            for (int i = 0; i < mLength - a.value.Length; i++)
            {
                aValue = "0" + aValue;
            }

            for (int i = 0; i < mLength - b.value.Length; i++)
            {
                bValue = "0" + bValue;
            }

            //główna pętla odejmowania
            for (int i = mLength - 1; i >= 0; i--)
            {
                //zamiana wartości z typu string do int
                aDigit = Convert.ToInt32(aValue[i].ToString());
                bDigit = Convert.ToInt32(bValue[i].ToString());

                //odejmowanie
                //pDigit jest najczęściej ujemne stąd + przy nim
                sum = aDigit - bDigit + pDigit;

                //"zabieranie 1 z następnej linii, aby móc wykonać odejmowanie
                if (sum < 0)
                {
                    sum += 10;
                    pDigit = -1;
                }
                else
                {
                    pDigit = sum / 10;
                }

                //dopisywanie wyniku z "jednej linii" do całości
                newValue = (sum % 10) + newValue;
            }

            //dopisywanie reszty z przodu, jeżeli jakaś została
            if (pDigit != 0)
            {
                newValue = pDigit + newValue;
            }
            
            //"obcinanie" zbędnych zer "z przodu" wyniku
            while (newValue[0] == '0' && newValue.Length > 1)
            {
                newValue = newValue.Remove(0, 1);
            }

            //przypisanie obliczonej wartości do wcześniej utworzonego obiektu
            result.value = newValue;


            //zwracenie obiektu
            return result;
        }
    }
}