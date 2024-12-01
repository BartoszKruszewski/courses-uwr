using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult Dynamic()
        {
            ViewBag.Layout = "_AlternateLayout";
            return View();
        }
        public ActionResult Partial()
        {
            var model = new MyModel { SomeProperty = "To jest przyk³adowa w³aœciwoœæ." };
            return View(model);
        }

		public ActionResult Section()
		{
			return View();
		}
	}

}
