class Document:
    def __init__(self , emloyeeName):
        self.EmloyeeName = emloyeeName

class Employee:
    def __init__(self, name):
        self.name = name
    def work(self , office):
        for i in range(0,10):
            office.documents.append(Document(self.name))

class Cleaner:
    def __init__(self, name):
        self.name = name
    def clean(self , office):
        print("clean")

class Manager:
    def __init__(self, name):
        self.name = name
        self.emloyees = []
    def hireEmployee(self,name):
        self.emloyees.append(Employee(name))
    def askEmployeesToWork(self,office):
        for employee in self.emloyees:
            employee.work(office)

class Office:
    def __init__(self):
        self.managers = []
        self.documents = []
        self.cleaners = []
    def hireManager(self,name):
        self.managers.append(Manager(name))
    def hireCleaner(self,name):
        self.cleaners.append(Cleaner(name))
    def startWorkDay(self):
        for manager in self.managers:
            employee.askEmployeesToWork(office)
        for cleaner in self.cleaners:
            cleaner.clean()



