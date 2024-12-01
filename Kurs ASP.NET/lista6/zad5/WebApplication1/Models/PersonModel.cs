namespace WebApplication1.Models
{
    public class PersonModel
    {
        [Pesel(ErrorMessage = "Numer PESEL jest niepoprawny.")]
        public string Pesel { get; set; }

        [AlphaNumericPolishAndWhitespace(ErrorMessage = "Dozwolone są tylko litery, cyfry i białe znaki.")]
        public string Name { get; set; }
    }
}
