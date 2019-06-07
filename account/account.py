from transaction import Transaction
class Account():
    def __init__(self , name):
        self.name = name
        self.transactions = []
    
    def addTransaction(self, description,amount):
        self.transactions.append(Transaction(description , amount))
    
    def getBalance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance


if __name__ == "__main__":
    newAcount = Account("Jien")
    newAcount.addTransaction("Car" , -90000)
    newAcount.addTransaction("salary" , 10000)
    newAcount.addTransaction("food" , -100)
    newAcount.addTransaction("salary" , 10000)
    newAcount.addTransaction("food" , -100)
    newAcount.addTransaction("salary" , 10000)
    newAcount.addTransaction("food" , -100)
    newAcount.addTransaction("salary" , 10000)
    balance = newAcount.getBalance()
    print(balance)


    
