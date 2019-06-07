from person import Person
from emloyee import Employee
class Manager(Person):
    def __init__(self,name):
        super().__init__(name)
        self.employees = []
    
    def hireEmployee(self,name):
        employee = Employee(name)
        self.employees.append(employee)
        return employee
    
    def work(self,office):
        for emp in self.employees:
            emp.work(office)

    def __eq__(self,object):
        return self.name == object.name

    if __name__ == "__main__":
        print("yo")
        manager= Manager("ss")
        print(manager.name)