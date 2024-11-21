using Microsoft.AspNetCore.Mvc;

namespace WebApplication1.Models
{
    public class FormModel
    {
        public string Name { get; set; }
        public bool IsActive { get; set; }
        public string Password { get; set; }
        public string Gender { get; set; }
        public string Description { get; set; }
        public int SelectedCategory { get; set; }
        public List<Category> Categories { get; set; }
    }

    public class Category
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }
}
