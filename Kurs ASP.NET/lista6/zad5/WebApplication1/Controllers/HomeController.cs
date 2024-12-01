using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Submit(PersonModel model)
        {
            if (ModelState.IsValid)
            {
                return Content("Dane s¹ poprawne.");
            }
            else
            {
                return View("Index", model);
            }
        }
    }
}
