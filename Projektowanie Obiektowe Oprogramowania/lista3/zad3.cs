// dotnet script zad3.cs

var items = new[]
{
    new Item { Name = "Telefon", Price = 2000m },
    new Item { Name = "Słuchawki", Price = 200m },
    new Item { Name = "Aparat", Price = 1500m }
};

var register1 = new CashRegister(
    new BasicTaxCalculator(),
    new SimpleBillPrinter()
);
Console.WriteLine("\n--- Kasa #1 ---");
Console.WriteLine($"Suma: {register1.CalculatePrice(items)}");
register1.PrintBill(items);

var register2 = new CashRegister(
    new ReducedTaxCalculator(),
    new AlphabeticalBillPrinter()
);
Console.WriteLine("\n--- Kasa #2 ---");
Console.WriteLine($"Suma: {register2.CalculatePrice(items)}");
register2.PrintBill(items);


public interface ITaxCalculator
{
    decimal CalculateTax(decimal price);
}

public interface IBillPrinter
{
    void PrintBill(IEnumerable<Item> items, ITaxCalculator taxCalculator);
}

public class Item
{
    public decimal Price { get; set; }
    public string Name { get; set; }
}

public class BasicTaxCalculator : ITaxCalculator
{
    public decimal CalculateTax(decimal price)
    {
        return price * 0.22m;
    }
}

public class ReducedTaxCalculator : ITaxCalculator
{
    public decimal CalculateTax(decimal price)
    {
        return price * 0.08m;
    }
}

public class SimpleBillPrinter : IBillPrinter
{
    public void PrintBill(IEnumerable<Item> items, ITaxCalculator taxCalculator)
    {
        Console.WriteLine("=== Proste drukowanie ===");
        foreach (var item in items)
        {
            Console.WriteLine("Towar: {0}, cena: {1}, podatek: {2}",
                                item.Name,
                                item.Price,
                                taxCalculator.CalculateTax(item.Price));
        }
    }
}

public class AlphabeticalBillPrinter : IBillPrinter
{
    public void PrintBill(IEnumerable<Item> items, ITaxCalculator taxCalculator)
    {
        Console.WriteLine("=== Drukowanie (sortowanie alfabetyczne) ===");
        var sorted = items.OrderBy(i => i.Name);

        foreach (var item in sorted)
        {
            Console.WriteLine("Towar: {0}, cena: {1}, podatek: {2}",
                                item.Name,
                                item.Price,
                                taxCalculator.CalculateTax(item.Price));
        }
    }
}

public class CashRegister
{
    private readonly ITaxCalculator _taxCalculator;
    private readonly IBillPrinter _billPrinter;

    public CashRegister(ITaxCalculator taxCalculator, IBillPrinter billPrinter)
    {
        _taxCalculator = taxCalculator;
        _billPrinter = billPrinter;
    }

    public decimal CalculatePrice(Item[] items)
    {
        decimal totalPrice = 0;
        foreach (var item in items)
        {
            totalPrice += item.Price + _taxCalculator.CalculateTax(item.Price);
        }
        return totalPrice;
    }

    public void PrintBill(Item[] items)
    {
        _billPrinter.PrintBill(items, _taxCalculator);
    }
}
