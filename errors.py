 
try:
    x=  input("enter a number: ")
    x = int(x)
    assert (x < 5), "Number should be bigger than 5"
    if (x < 5),
        raise Exception("Number should be bigger than 5")
except ValueError as err:
    print("line 9 trying to get a number from a user  - failed") #The number should be smaller than 10
except ZeroDivisionError as err:
    print("line 9 trying to get a number from a user should be different from 0  - failed") #The number should be smaller than 10
except Exception as err:
    print(err) #The number should be smaller than 10
else:
    # not safe code 
    print("not safe code ")

print("end of code")