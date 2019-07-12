class User():
    def __init__(self , firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

        
    def serialize(self):  
        return {           
            'firstName': self.firstName, 
            'lastName': self.lastName
        }