using Microsoft.AspNetCore.Mvc;
using System.Data.SqlClient;
using WebApplication1.Services;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        private readonly IDbConnectionService _dbConnectionService;

        public HomeController(IDbConnectionService dbConnectionService)
        {
            _dbConnectionService = dbConnectionService;
        }

        public IActionResult Index()
        {
            // U¿ycie symulowanych danych
            if (_dbConnectionService is MockDbConnectionService mockService)
            {
                var data = mockService.GetMockData();
                ViewData["UserName"] = data.First()["Name"];
            }
            else
            {
                ViewData["UserName"] = "Brak danych";
            }

            return View();
        }
    }

}
