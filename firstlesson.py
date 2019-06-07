
# def getAvg(lst):
#     sum = 0
#     for i in range(len(lst)):
#         sum += lst[i]
#     return (sum/len(lst))
#J
def createFibonachi():
    n1 = 0
    n2 = 1
    fib = []
    for i in range(10):
        #print(n1, end=",")
        fib.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
    print(fib)
    return fib

fib = createFibonachi()
num = input("Enter a number: ")
isFib = False
for j in fib:
    #print("j: ", type(j))
    if int (num) == j:
        print(num, " is in fibonacci")
        isFib = True

if (not isFib):
    print(num, "Is NOT in Fibonacci")




def isNumberInList(lst , n): 
    for i in range(len(lst)):
        if (lst[i] == n)
            return true 
    return false

lst = []
itm = input("Insert an number: ")
while (itm.isdigit()):
    lst.append(int(itm))
    itm = input("Insert an number: ")

# # print("avg: " , getAvg(lst))



