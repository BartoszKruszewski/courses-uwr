using WebApplication1.Models;
using WebApplication1.Data;
using Microsoft.EntityFrameworkCore;


namespace WebApplication1.Data
{
    public class StudentRepository
    {
        private readonly ApplicationDbContext _context;

        public StudentRepository(ApplicationDbContext context)
        {
            _context = context;
        }

        // Pobierz wszystkich studentów
        public IEnumerable<Student> GetAll()
        {
            return _context.Students.ToList();
        }

        // Pobierz studenta po ID
        public Student GetById(int id)
        {
            return _context.Students.Find(id);
        }

        // Dodaj nowego studenta
        public void Add(Student student)
        {
            _context.Students.Add(student);
            _context.SaveChanges();
        }

        // Zaktualizuj istniejącego studenta
        public void Update(Student student)
        {
            _context.Students.Update(student);
            _context.SaveChanges();
        }

        // Usuń studenta
        public void Delete(int id)
        {
            var student = _context.Students.Find(id);
            if (student != null)
            {
                _context.Students.Remove(student);
                _context.SaveChanges();
            }
        }
    }
}
