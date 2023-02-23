from fileinput import filename
import json
import os
from xml.dom.minidom import Element

def directory_exist():
    while True:
        gg = input("what name for your new directory ? ")
        path = 'C://Users//clem//'+ gg +'//'
        isFile = os.path.isdir(path)
        if not isFile: 
            try: 
                os.makedirs(gg)
                print(f"file {gg} created!!")
                return gg
                
            except FileExistsError:
                u = input("Already existing!! Do you wish to continue with this directory? yes or no?")
                if u == "yes":
                    break
                if u == "no":
                    continue
                else:
                    return directory_exist()
        else:
            print("this directory already exit !!")
            return directory_exist()
    return gg   

def reading(label, element, personne):
    a = input(label) 
    if a == "":
        return reading(label, element, personne)
    elif a == "exit":
        exit(0)
    else:
        personne[element] = a
        return 

def reading2(label, element, personne):
    while True:
        c = input(label)
        if c == "":
            return reading2(label, element, personne)
        if c == "exit":
            exit(0)       
        if 18 < int(c) < 65:
            personne[element] = int(c)
            break
        else:
            print("you should get an age beetween 18 and 65 years!!")
            continue 
    return personne
    

def include_person():
    while True:
        gg = input("which directory (name) you which to include files ?")
        lalist = []
        json_file = input("put the name of your file you want include or put exit!")
        if json_file == "exit":
            break
        filename = 'C://Users//cleme//'+ str(gg) +'//'+ str(json_file) + '.json'
        if os.path.lexists(filename):
            print("this document already exit !! put another name please")
            continue
        
        else:
            personne = {}
            reading("your firstname?","first name", personne)
            reading("your last name?", "last name", personne)
            reading2("your age?", "age", personne)

            d = input("your professional ID ?")
            if d == "exit":
                exit(0)
            elif len(d) == 8:
                personne["professionnal ID"] = d
                print("all correctly installed!! thank you!!")
            else:
                print("your ID must get a lenght of 8 characters and only uppercase letters!! begin again")
            lalist.append(personne)
            person_json = json.dumps(lalist)
            f = open(filename, "w")
            f.write(person_json)
            f.close()
        g = input("will you break ?")
        if g == "break":
            break
    return lalist

def delete():
    gg = input("which directory (name) you which to modify files ?")
    tt = input("which file you'd like to cancel ?")
    filename = 'C://Users//cleme//'+ str(gg) +'//'+ str(tt) + '.json'
    if os.path.lexists(filename + str(tt)):
        return delete(filename)
    os.remove(filename)
    print("your file is cancelled !!")
    return

def read():
    h = input("which directory you wish read ? ")
    path = 'C://Users//cleme//'+ h +'/'
    for i in os.listdir(path):
        f = open(path+i, "r")
        donnees_json = f.read()
        f.close()
        oo = json.loads(donnees_json)
        print(oo)

def stop_app():
    return exit(0)

def reduce_updating(lalist, B, C):
    while True:
        if B == "age":
            age = input(C)
            if age == "nope":
                break
            chars = set('0123456789')
            if any((c in chars) for c in age):
                for i in range(len(lalist)):          
                    lalist[i]["age"] = age
                break
            print("found characters we don't want!! do it again!! only numbers!!")

        A = input(C)
        chars = set('0123456789$%*£)_\//-+=!,')
        if B == "professionnal ID":
            chars = set('())_\//-+=!,')    
        if not any((c in chars) for c in A):
            if A == "nope":
                break
            for i in range(len(lalist)):
                lalist[i][B] = A
            break
        print("found characters we don't want!! do it again!!")
    return lalist


def update():
    while True:
        gg = input("which directory (name) you which to modify files ?")
        aa = input("name of the file you want to modify please ?")
        filename = 'C://Users//cleme//'+ gg +'//'+ aa + '.json' 
        if os.path.lexists(filename):
            f = open(filename, "r")
            donnees_json = f.read()
            f.close()
            lalist = json.loads(donnees_json)
            print(lalist)
            reduce_updating(lalist, "first name", "will you change the first name ? if yes put the new first name, if not put nope")
            reduce_updating(lalist, "last name", "will you change the last name ? if yes put the new last name, if not put nope")
            reduce_updating(lalist, "age", "will you change the age ? if yes put the age, if not put nope")
            reduce_updating(lalist, "professionnal ID", "will you change the professionnal ID ? if yes put the new professionnal ID, if not put nope")
            person_json = json.dumps(lalist)
            f = open(filename, "w")
            f.write(person_json)
            f.close()
            k = input("will continue or stop to modify records ?")
            if k == "continue":
                 update()
            elif k == "stop":
                break
        else:
            update()
  
    return lalist   


while True:
    T = input("What do want to do : create new directory, delete, update, list, include or stop ?")
    if T == "delete":
        delete()
        continue
    if T == "create new directory":
        directory_exist()
    if T == "update":
        update()
        continue
    if T == "list":
        read()
        continue
    if T == "include": 
        include_person()
        continue
    if T == "stop":
        stop_app()
    if not T == "stop" and not T == "include" and not T == "list" and not T == "update" and not T == "create new directory" and not T == "delete":
        continue