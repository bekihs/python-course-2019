print(__name__)

class User():

    def __init__(self, name , startYear):
        self.name = name
        self.startYear = startYear
        self.courses = []
    
    def addCourse(course):
        self.courses.append(course)

class Student(User):

    def __init__(self, name, startYear):
         super().__init__( name, startYear)
         self.grades = []

    def receiveGrade(self,grade):
        self.grades.append(grade)

class Teacher(User):

    def __init__(self, name, startYear, salary):
         super().__init__( name, startYear)
         self.salary =salary

    def giveGrade(self,student,grade):
        student.receiveGrade(grade)



s1 = Student("Ronda", 2017)
t1 = Teacher("Cassandra", 2002, 40000)

t1.giveGrade(s1,  82)
firstGrade = s1.grades[0]

print('{} received an {} in the last test'.format(s1.name,firstGrade ))
#above should print "Ronda received an 82 in the last test"