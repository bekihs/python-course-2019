Deliveries= {
     "Noam": {"claimed": False},
     "Dana": {"claimed":True}
}
 
def claimDelivery(name):
   print("function claim")
   #Write your code here
#    if (deliveries[name] == None)
#         return True
#     else:
#         return False
 
firstName = input("please enter a name")
while firstName != "stop":
   result = claimDelivery(firstName)
   print(result)
   firstName = input("please enter a name")
