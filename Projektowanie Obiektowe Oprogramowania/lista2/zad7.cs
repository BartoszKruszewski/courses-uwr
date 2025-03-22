// dotnet script zad7.cs

var courses = new List<Course>
{
    new Course("Matematyka", 4.5),
    new Course("Fizyka", 3.8),
    new Course("Informatyka", 5.0)
};

var student = new Student("Jan Kowalski", courses);
var gradeController = new GradeController();
var usosWebPage = new UsosWebPage(gradeController);

usosWebPage.Show(student);

class Student
{
    public string Name { get; }
    public List<Course> Courses { get; }

    public Student(string name, List<Course> courses)
    {
        Name = name;
        Courses = courses;
    }

    public List<Course> GetCourses()
    {
        return Courses;
    }
}

class Course
{
    public string Name { get; }
    public double Grade { get; }

    public Course(string name, double grade)
    {
        Name = name;
        Grade = grade;
    }

    public double GetValue()
    {
        return Grade;
    }
}

class GradeController
{
    public Dictionary<string, double> GetStudentGradeInfo(Student student)
    {
        var grades = new Dictionary<string, double>();
        var courses = student.GetCourses();

        foreach (var course in courses)
        {
            grades[course.Name] = course.GetValue();
        }

        return grades;
    }
}

class UsosWebPage
{
    private readonly GradeController _gradeController;

    public UsosWebPage(GradeController gradeController)
    {
        _gradeController = gradeController;
    }

    public void Show(Student student)
    {
        var studentGradeInfo = _gradeController.GetStudentGradeInfo(student);
        Console.WriteLine($"Oceny studenta {student.Name}:");
        foreach (var entry in studentGradeInfo)
        {
            Console.WriteLine($" - {entry.Key}: {entry.Value}");
        }
    }
}
