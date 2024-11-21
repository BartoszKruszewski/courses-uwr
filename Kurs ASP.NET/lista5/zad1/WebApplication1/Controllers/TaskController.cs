using System.Web.ModelBinding;
using System.Web.Mvc;


namespace WebApplication1.Controllers
{
    public class TaskController
    {
        public class TaskController : Controller
        {
            // Action to display the form
            public ActionResult Index()
            {
                return View();
            }

            // Action to process the form
            [HttpPost]
            public ActionResult Index(TaskModel model)
            {
                if (ModelState.IsValid)
                {
                    // Optionally save or process the data
                    return View("Results", model); // Display results on a new page
                }

                // If the model is invalid, return to the form with error messages
                return View(model);
            }
        }
    }
}