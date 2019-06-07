from Course import Course
import datetime 
class Teacher():
    def __init__(self , name):
        self.name = name
        self.courses = []
    
    def startCourse(self,courseName, startDate):
        newCourse = Course(courseName , startDate ,self)
        self.courses.append(newCourse)
        return newCourse

    def gradeAllStudents(self , grad):
        for course in self.courses:
            for student in course.students:
                student.grades[course.name] = grad



hadas = Teacher("hadas")
hadas.startCourse("python" , datetime.datetime.now())