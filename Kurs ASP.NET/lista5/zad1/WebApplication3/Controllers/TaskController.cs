using System.Web.Mvc;
using WebApplication3.Models;

namespace WebApplication3.Controllers
{
    public class TaskController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public ActionResult Index(TaskModel model)
        {
            if (ModelState.IsValid)
            {
                return View("Results", model);
            }
            return View(model);
        }
    }
}