using Microsoft.AspNetCore.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class TaskController : Controller
    {
        [HttpGet]
        public IActionResult Index()
        {
            return View();
        }
        
        [HttpPost]
        public IActionResult Submit(TaskModel model)
        {
            if (ModelState.IsValid)
            {
                return View("Results", model);
            }

            return View("Index", model);
        }
    }
}
