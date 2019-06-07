
class Animal():
    # class attribute
    animalsCount = 0
    # The Constructor - Initializer / Instance Attributes
    def __init__(self, type, name, age):
        self.name = name
        self.age = age
        self.type = type 
        Animal.animalsCount+=1

    def description(self):
        return "{} is a {} years old {}".format(self.name , self.age,self.type)
    
    @classmethod
    def printCount(cls):
        print(cls.animalsCount , " " , cls.__name__, " out of " , Animal.animalsCount ,"animals in the worls")
 

newAnimal = Animal("dog","chichi",2)
dog1 = Animal("dog","chichi",2)
Animal.printCount()

class Cat(Animal):
    animalsCount = 0
    # Overriding the constructor    
    def __init__(self, name, age, isStreetCat):
         super().__init__("Cat",name, age)
         self.isStreetCat = isStreetCat
         Cat.animalsCount += 1
         
         
    def description(self):
        desc = super().description()
        if self.isStreetCat:
            desc += " that lives in the streets"
        return desc

roni = Cat("Roni",1 , True)      
print(roni.description())#Roni is a 1 years old Cat that lives in the streets
Cat.printCount()

# print(roxy.description())#Roxy is a 3 years old Dog

# roxy.birthday()
# print(roxy.age) #4 

