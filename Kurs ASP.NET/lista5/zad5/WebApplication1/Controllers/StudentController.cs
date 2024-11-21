using Microsoft.AspNetCore.Mvc;
using WebApplication1.Data;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class StudentController : Controller
    {
        private readonly StudentRepository _repository;

        public StudentController(StudentRepository repository)
        {
            _repository = repository;
        }

        public IActionResult Index()
        {
            var students = _repository.GetAll();
            return View(students);
        }

        public IActionResult Edit(int id)
        {
            var student = _repository.GetById(id);
            if (student == null)
            {
                return NotFound();
            }
            return View(student);
        }

        [HttpPost]
        public IActionResult Edit(int id, Student student)
        {
            if (id != student.Id)
            {
                return BadRequest();
            }

            _repository.Update(student);
            return RedirectToAction(nameof(Index));
        }

        public IActionResult Delete(int id)
        {
            var student = _repository.GetById(id);
            if (student == null)
            {
                return NotFound();
            }
            return View(student);
        }

        [HttpPost, ActionName("Delete")]
        public IActionResult DeleteConfirmed(int id)
        {
            _repository.Delete(id);
            return RedirectToAction(nameof(Index));
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(Student student)
        {
            _repository.Add(student);
            return RedirectToAction(nameof(Index));
        }
    }
}
