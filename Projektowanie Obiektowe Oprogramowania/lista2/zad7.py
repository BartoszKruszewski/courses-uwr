class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def getCourses(self):
        return self.courses


class Course:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getValue(self):
        return self.grade


class GradeController:
    def getStudentGradeInfo(self, student):
        grades = {}
        courses = student.getCourses()
        for course in courses:
            course_data = course.getAll(student)
            grade_value = course_data.getValue()
            grades[course.name] = grade_value
        return grades


class UsosWebPage:
    def __init__(self, grade_controller):
        self.grade_controller = grade_controller

    def show(self, student):
        student_grade_info = self.grade_controller.getStudentGradeInfo(student)
        print(f"Oceny studenta {student.name}:")
        for course_name, grade in student_grade_info.items():
            print(f" - {course_name}: {grade}")
