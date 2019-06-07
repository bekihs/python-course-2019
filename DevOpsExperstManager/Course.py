class Course():
    def __init__(self , name , startDate , teacher):
        self.name = name
        self.students = []
        self.startDate = startDate
        self.Teacher = teacher
    
    def addStudentToCourse(self,student):
        self.students.append(student)
 
