name = "hadas"
email = "hh@hh.hh"
phone = ["05222222", "7879878979"]

hadas = {'name': name,
"age": 8, 
"isAdult": False,
"address": {"city":"TA", "street":"Shenkin" , "number":7, "appartment":6},
'email': 'hh@hh.hh', 
'phone': ['05222222', "03444444"]}
# hadas = {}
# hadas["email"] = "hh@hmail.com"
# hadas["hairColor"] = "black"
# hadas["phone"] = ["0522234567"]
# hadas["phone"].insert(0,"066768")

dana = {'name': "dana",
"age": 10, 
"isAdult": False,
"address": {"city":"Karmiel", "street":"Shenkin" , "number":7, "appartment":6},
'email': 'hh@hh.hh', 
'phone': ['05222222', "03444444"]}
shani = {'name': "shani",
"age": 9, 
"isAdult": False,
"address": {"city":"BS", "street":"Shenkin" , "number":7, "appartment":6},
'email': 'hh@hh.hh', 
'phone': ['05222222', "03444444"]}

kids = [hadas,dana,shani]
print(kids)

for item in kids:
    print(item["name"])

hadasMail = [kid["email"] for kid in kids if kid["name"] == "hadas"] 

for kid in kids:
    if kid["name"] == "hadas":
        print(kid["email"])

# address = person["address"]
# print(person["address"]["city"])
# print(person["address"]["street"])
# print(person["phone"][0])


users = {"hadas": {} , "dana":{}, "dan" : {},"hadas":{}}
users["Roi"] = {}
users["hadas"]["name"] = "hadas"
users["hadas"]["age"] = 8
users["hadas"]["email"] = "hh@gmail.com"
print(users)
 
 




