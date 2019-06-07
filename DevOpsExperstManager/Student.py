class Student():
    def __init__(self , name):
        self.name = name
        self.courses = []
        self.grades = {}
        
    def joinCourse(self,course):
        self.courses.append(course)
        course.addStudentToCourse(self)
 
