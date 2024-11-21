using System.ComponentModel.DataAnnotations;

namespace WebApplication1.Models
{
    public class TaskModel
    {
        [Required(ErrorMessage = "First name is required.")]
        public string? FirstName { get; set; }

        [Required(ErrorMessage = "Last name is required.")]
        public string? LastName { get; set; }

        [Required(ErrorMessage = "Tasks are required.")]
        public List<string> Tasks { get; set; } = new List<string>(new string[10]);
    }
}
