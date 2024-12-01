using Microsoft.AspNetCore.Mvc;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class PageController : Controller
    {
        public IActionResult Render(string siteName, string pageName)
        {
            var model = new PageViewModel
            {
                SiteName = siteName,
                PageName = pageName,
                Content = $"This is the content for the page '{pageName}' on site '{siteName}'."
            };


            return View(model);
        }
    }
}
