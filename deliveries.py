Deliveries= {
     "Noam": {"claimed": False},
     "Dana": {"claimed":True}
}
 
def claimDelivery(name):
    name = name.lower().capitalize()
    #Write your code here
    if name in Deliveries:
        delivery = Deliveries[name]
        if delivery["claimed"]: #Deliveries[name]["claimed"]
           print("You already took your delivery")
           return True
        else:
           delivery["claimed"] = True
           print("Here is your delivery")
           return True
    else:
        Deliveries[name] = {"claimed":False}
        print("Hey {}, We've created a delivery for you".format(name))
        return False

 
firstName = input("please enter a name: ")
while firstName != "stop":
   result = claimDelivery(firstName)
   print(result)
   firstName = input("please enter a name")
