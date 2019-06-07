from Course import Course
from Teacher import Teacher
from Student import Student
import datetime 

hadas = Teacher("hadas")
eddie = Teacher("eddie")

christina = Student("christina")
Tal = Student("Tal")
Ifat = Student("Ifat")
Amit = Student("Amit")
Amir = Student("Amir")
Tamir = Student("Tamir")

python1 = hadas.startCourse("python_2019" , datetime.datetime.now())
python2 = hadas.startCourse("python_2020" , datetime.datetime(2020, 5, 17))


devOps1 = eddie.startCourse("devOps_2019" , datetime.datetime.now())
devOps2 = eddie.startCourse("devOps_2020" , datetime.datetime(2020, 5, 17))


Amir.joinCourse(python1)
Amir.joinCourse(devOps2)

Tamir.joinCourse(python1)
Tamir.joinCourse(python2)

Amit.joinCourse(devOps1)
Ifat.joinCourse(devOps1)
Tal.joinCourse(python1)

hadas.gradeAllStudents(100)
eddie.gradeAllStudents(70)
