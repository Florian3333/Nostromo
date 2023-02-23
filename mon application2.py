import json
import os


filename = 'C://Users//cleme//json_file.json'
dd = os.path.lexists(filename)
# zz = input("put 'pass' to stop the asking listing or put 'list' if you want list of all !")


if dd:
    f = open(filename, "r")
    donnees_json = f.read()
    f.close()
    oo = json.loads(donnees_json)
    print(oo)
else:
    f = open(filename, "w")
    f.write()
    f.close()
    oo = []

ff = int(input("how many persones you want include in ?"))
lalist = oo
l = 0
while not l == ff: 
    personne = {}
    a = input("your firstname?")
    if a == "":
        continue
    elif a == "exit":
        exit(0)
    else:
        personne["first name"] = a

    b = input("your last name?")
    if b == "":
        continue
    elif b == "exit":
        exit(0)
    else:
        personne["last name"] = b

    c = input("your age ?")
    if c == "exit":
        exit(0)       
    elif 18 < int(c) < 65:
        personne["age"] = c
    else:
        print("you should get an age beetween 18 and 65 years!!")
        continue  

    d = input("your professional ID ?")
    if d == "exit":
        exit(0)
    elif len(d) == 8:
        personne["professionnal ID"] = d
        print("all correctly installed!! thank you!!")
    else:
        print("your ID must get a lenght of 8 characters and only uppercase letters!! begin again")
    lalist.append(personne)
    l = l + 1

command = input("press 'delete' to cancel a profile or 'update' to update a profile?")
if command == "delete":
    while True:
        local_permission = input("what is your professionnal ID to cancel the profil ?")
        for i in range(len(lalist)):
                print("personne n°:", str(i+1) + "  " + lalist[i]["professionnal ID"])
        i = 0
        while i < len(lalist):           
            if local_permission == lalist[i]["professionnal ID"]:
                break       
            i = i + 1                
        cancel_profil = int(input("which profile you wish to erase?"))
        lalist.remove(lalist[cancel_profil-1])
        u = input("do you continue or stop?")
        if u == "continue":
            continue
        if u == "stop":
            break


for i in range(len(lalist)):
    print(("first name person N° "+ str(i+1) + ": "+ lalist[i]["first name"]), ("last name person N° " + str(i+1) + ": "+ lalist[i]["last name"]), ("age person N° " + str(i+1) + ": " + lalist[i]["age"]), ("professionnal ID person N° " + str(i+1) + ": " + lalist[i]["professionnal ID"]))


if command == "update":
    change_profile = input("what is your professionnal ID to change information of the profil ?")
    for i in range(len(lalist)):
        if change_profile == lalist[i]["professionnal ID"]:
            cc = input("which profile you will change ?")

    for i in range(len(lalist)):
        if cc == lalist[i]["professionnal ID"]:  
            first_name = input("will you change the first name ? if yes put the new first name, if not put nope")
            last_name = input("will you change the last name ? if yes put the new last name, if not put nope")
            age = input("will you change the age ? if yes put the new age, if not put nope")
            pro_id = input("will you change the professionnal id ? if yes put the new professionnal id, if not put nope")
                
            if first_name == "nope":
                pass
            else:
                lalist[i]["first name"] = first_name

            if last_name == "nope":
                pass
            else:
                lalist[i]["last name"] = last_name

            if age == "nope":
                pass
            else:
                lalist[i]["age"] = age
            
            if pro_id == "nope":
                pass
            else:
                lalist[i]["professionnal ID"] = pro_id


print("the actual list is now: ", lalist)
                
person_json = json.dumps(lalist)
f = open(filename, "w")
f.write(person_json)
f.close()