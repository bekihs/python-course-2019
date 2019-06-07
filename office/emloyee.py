from document import Document
from person import Person

class Employee(Person): 
    def work(self, aRandomOffice):
        for i in range(0,10):
            newDocument = Document(self.name)
            aRandomOffice.documents.append(newDocument)

if __name__ == "__main__":
    glassesOffice = Office("glasses")
    freeLancer = Employee("Boris")
    freeLancer.work(glassesOffice)
    print(len(glassesOffice.documents))
