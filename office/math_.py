from manager import Manager
from emloyee import Employee
import pytest

class TestClass_Manager():

    def test_string(self):
        with pytest.raises(Exception):
            Manager("Galia")

    def test_number(self):  
        with pytest.raises(Exception):
            Manager(1)

    def test_list(self):  
        with pytest.raises(Exception):
            Manager([5,3,8,7,6])
    
    def test_office(self):
        galia = Manager("galia")
        newOffice = Office()
        with pytest.raises(Exception): 
            galia.work(5)
            galia.work([1,2,3])
            galia.work(Office())
            
    
    def test_employeeLst(self):
        galia = Manager("Galia")
        assert galia.employees == []
    #Can't deal with the super when I want to create a manager!!


    def test_hireEmployee(self):
        bob = Manager("bob")
        galia = bob.hireEmployee("Galia")
        assert galia == Employee("Galia")
    #Same issue!


if __name__ == "__main__":
    galia = Manager("galia")