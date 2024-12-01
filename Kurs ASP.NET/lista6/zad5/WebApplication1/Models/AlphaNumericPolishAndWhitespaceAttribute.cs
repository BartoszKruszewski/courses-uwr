using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text.RegularExpressions;

namespace WebApplication1.Models
{
    public class AlphaNumericPolishAndWhitespaceAttribute : ValidationAttribute
    {
        public override bool IsValid(object value)
        {
            if (value == null)
                return false;

            string input = value.ToString();

            // Wyrażenie regularne dopuszczające litery, cyfry i białe znaki
            string pattern = @"^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ0-9\s]*$";
            return Regex.IsMatch(input, pattern);
        }
    }
}
