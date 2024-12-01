using System.ComponentModel.DataAnnotations;

namespace WebApplication1.Models
{
    public class PeselAttribute : ValidationAttribute
    {
        public override bool IsValid(object value)
        {
            if (value == null)
                return false;

            string pesel = value.ToString();

            return (pesel.Length == 11 && pesel.All(char.IsDigit));
        }
    }
}
