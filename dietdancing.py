import sqlite3
import os

def Body_Mass_Index(weight, size):
    BMI = weight / (size*size) 
    print('your BMI is ' + str(BMI))
    if BMI < 18.5:
        print('you are in underweight situation !')
    elif 18.5 < BMI < 24.9:
        print('you are in a normal weight situation')
    elif 25 < BMI < 29.9:
        print('you are considered as overweighted')
    elif 30 < BMI < 34.9:
        print('you are considered as obese of class I')
    elif 35 < BMI < 39.9:
        print('you are considered as obese of class II')
    else:
        print('you are considered as obese of class III(morbid)')


def liste(cur):
    cur.execute("SELECT * FROM meal")
    resultats = cur.fetchall()
    for resultat in range(len(resultats)):
        print('Number:'+ str(resultat + 1) + '=' + str(resultats[resultat]))

def weight_target(): 
    project = weight - losing_weight_target
    print(f"you project is to lose {project} kg.")
    return project

def acces_authorized():
    if input("professionnal part need a password") in ('superman'):
        return True
    
def database_system():
    conn = sqlite3.connect('mickey.db')
    cur = conn.cursor()
    if not os.path.exists('mickey.db'):
    # Création d'une table dans la base de données
        cur.execute('''CREATE TABLE meal
                (ingedient TEXT, calories FLOAT)''')
        
    cc = '' 
    while cc != 'stop':
        cc = input('que veut tu inserer?')
        gg = cc.split()
        if len(gg) == 2:
            # Insertion de données dans la table
            cur.execute(f"INSERT INTO meal (ingedient, calories) VALUES ('{gg[0]}', {int(gg[1])})")
        elif len(gg) == 1:
            if gg[0] == 'list':
                liste(cur)
            if gg[0] == 'delete':
                ss = int(input('which one you will camcel from the list?'))
                cur.execute('DELETE FROM meal WHERE rowid=?', (ss,))
                print('canceled element from your database')
    # Ferme le curseur et la connexion à la base de données
    conn.commit()
    cur.close()
    conn.close()

def food_calories_quantification():
    conn = sqlite3.connect('mickey.db')
    cursor = conn.cursor()
    ingred_quantity = ''
    while ingred_quantity != 'stop':
        ingred_quantity = input('what did you eat today ?(must be separated with a space and place their quanties in grammes for each of them')
        ff = ingred_quantity.split()
        if ff[0] == 'list': 
            liste(cursor)
            cursor.execute("SELECT * FROM meal WHERE name = ?", (ff[0],))
            result = cursor.fetchone()
    conn.close()
    print(result)



pro_or_users = ''
while pro_or_users != 'finish':
    pro_or_users = input('are you client or programors\'s crew put crew or client')
    if pro_or_users == "crew":
        if acces_authorized():
            Pro_database = database_system()
    if pro_or_users == "client":
        weight = float(input('what is your current weight ?'))
        size = float(input('what is your size ?'))
        Body_Mass_Index(weight, size)
        losing_weight_target = float(input('what is your weight target (say about the final result in Kg you desire to aim)?'))
        project = weight_target()
        food_calories_quantification()
