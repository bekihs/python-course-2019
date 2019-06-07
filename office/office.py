from manager import Manager
from cleaner import Cleaner
from emloyee import Employee

class Office():
    def __init__(self, name):
        self.name = name
        self.documents = []
        self.managers = []
        self.cleaners = []

    def hireManager(self, name):
        newEmployee = Manager(name)
        self.managers.append(newEmployee)

    def hireCleaner(self, name):
        newEmployee = Cleaner(name)
        self.cleaners.append(newEmployee)
    
    def startWorkDay(self):
        for manager in self.managers:
            manager.work(self)
        for cleaner in self.cleaners:
            cleaner.work()

if __name__ == "__main__":
    
    glassesOffice = Office("glasses")
    glassesOffice.hireManager("kj")
    glassesOffice.managers[0].name == "kj"

    freeLancer = Employee("Boris")
    freeLancer.work(glassesOffice)
    print(len(glassesOffice.documents))

    ToysAreUs = Office("ToysAreUs")
    freeLancer.work(ToysAreUs)
    
    manager  = Manager("Guri")
    manager.hireEmployee("kein")
    manager.hireEmployee("Dani")

    manager1  = Manager("Guri")
    manager1.hireEmployee("kein")
    manager1.hireEmployee("Dani")

    manager.work(glassesOffice)

    ToysAreUs.hireManager("Shlomi")
    ToysAreUs.managers[1].hireEmployee("kein")
    ToysAreUs.managers[1].hireEmployee("Hadas")
    ToysAreUs.hireCleaner("George")
    ToysAreUs.hireCleaner("Beni")
    ToysAreUs.hireCleaner("Loda")
    ToysAreUs.startWorkDay()
    print(len(ToysAreUs.documents))

    
