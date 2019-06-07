
class Person():
    
    peopleCount = 0
    # The Constructor - Initializer / Instance Attributes
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone 
        Person.peopleCount += 1
 
    def sayHello(self):
        print("Hello! I'm {}".format(self.name))

    def changeMail(self , newMail):
        self.email = newMail

    @classmethod
    def printPeopleCount(cls):
        print("There's {} eople n your program".format(cls.peopleCount))



class Student(Person):

    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone 

    def sayHello(self):
        print("hello")

    def askQuestion(self):
        print("?")

hadas = Student("hadas" , "ss@ff.ss" , "55675675")
print(hadas.sayHello())

hadas = Person("Hadas" , "hh@hh.com" , "049887280")
dana = Person("Dana" ,"uul" , "888")
dana.sayHello()
Person.printPeopleCount()
print(Person.peopleCount)
hadas.sayHello()
Person.peopleCount
hadas.changeMail("uu@u.hh")
hadas.email = "hadas@@gmail.com"
print(hadas.email)

hadas.height = 1.67
print(hadas.height)


dana = Person("Dana" , "dana@hh.com" , "0544765945")
print(hadas)

# class Cat(Animal):
#         # Overriding the constructor    
#     def __init__(self, name, age, isStreetCat):
#          super().__init__("Cat",name, age)
#          self.isStreetCat = isStreetCat
         
#     def description(self):
#         str = super().description()
#         if self.isStreetCat:
#             str += " that lives in the streets"
#         return str

# roni = Cat("Roni",1 , True)      
# print(roni.description())#Roni is a 1 years old Cat that lives in the streets


# print(roxy.description())#Roxy is a 3 years old Dog

# roxy.birthday()
# print(roxy.age) #4 

