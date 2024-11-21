using Microsoft.AspNetCore.Mvc;

namespace WebApplication1.Controllers
{
    public class FileController : Controller
    {
        private readonly IWebHostEnvironment _webHostEnvironment;

        public FileController(IWebHostEnvironment webHostEnvironment)
        {
            _webHostEnvironment = webHostEnvironment;
        }

        public IActionResult Upload()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Upload(IFormFile file)
        {
            if (file == null || file.Length == 0)
            {
                ViewBag.Message = "Wybierz plik do przesłania.";
                return View();
            }

            var uploadsFolderPath = Path.Combine(_webHostEnvironment.WebRootPath, "uploads");
            Directory.CreateDirectory(uploadsFolderPath);

            var filePath = Path.Combine(uploadsFolderPath, file.FileName);

            using (var stream = new FileStream(filePath, FileMode.Create))
            {
                await file.CopyToAsync(stream);
            }

            ViewBag.Message = $"Plik {file.FileName} został przesłany pomyślnie.";
            return View();
        }
        public IActionResult Download()
        {
            var uploadsFolderPath = Path.Combine(_webHostEnvironment.WebRootPath, "uploads");
            var files = Directory.GetFiles(uploadsFolderPath)
                                 .Select(Path.GetFileName)
                                 .ToArray();
            ViewBag.Files = files;
            return View();
        }

        [HttpPost]
        public IActionResult Download(string fileName)
        {
            var uploadsFolderPath = Path.Combine(_webHostEnvironment.WebRootPath, "uploads");
            var filePath = Path.Combine(uploadsFolderPath, fileName);

            if (!System.IO.File.Exists(filePath))
            {
                return NotFound();
            }

            var fileBytes = System.IO.File.ReadAllBytes(filePath);
            return File(fileBytes, "application/octet-stream", fileName);
        }
    }
}
