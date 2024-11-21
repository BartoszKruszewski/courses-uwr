using Microsoft.AspNetCore.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            var model = new FormModel
            {
                Categories = new List<Category>
                {
                    new Category { Id = 1, Name = "Technologia" },
                    new Category { Id = 2, Name = "Nauka" },
                    new Category { Id = 3, Name = "Kultura" }
                }
            };
            return View(model);
        }

        [HttpPost]
        public IActionResult Submit(FormModel model)
        {
            if (ModelState.IsValid)
            {
                // Przetwórz dane formularza
                return Content($"Dane: {model.Name}, {model.IsActive}, {model.Password}, {model.Gender}, {model.Description}, {model.SelectedCategory}");
            }
            return View("Index", model);
        }
    }
}
