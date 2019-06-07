 


person = {'firstName':"Hadas",'lastName':"shamir" , 'phone':"0000",'email':"ee@ee.ee"}
# lstSibling = ['shir','or','dana']
# person["sibling"] = lstSibling
person["sibling"] = ['shir','or','dana']



person["parents"] = [{'firstName':"mom",'lastName':"shamir" , 'phone':"6768678678",'email':"ee@ee.ee"},
{'firstName':"dad",'lastName':"shamir" , 'phone':"6768678678",'email':"ee1@ee.ee"},
{'firstName':"second mom",'lastName':"malka" , 'phone':"76768",'email':"ee8@ee.ee"}]

lstParents = person["parents"]
firstParent = lstParents[0] 


def printSiblingNames(person):
    [print(subling) for subling in person["sibling"]]
    print(person["sunbling"])


def searchParent(person , parentFIrstName):
    return false