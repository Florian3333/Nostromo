import datetime
import calendar
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import os
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

def pdf_report(current_date, modeles, nombres):
    # Création de la classe PDF personnalisée
    class PDF(FPDF):
        def header(self):
            pass
        
        def footer(self):
            pass

    # Création de l'objet PDF
    pdf = PDF()

    # Ajout d'une page
    pdf.add_page()

    # Définition des dimensions de la cellule du tableau
    cell_width = 40
    cell_height = 10

    # Définition du titre
    titre = f"Budget for the {str(current_date)}"

    # Création du titre en gras
    pdf.set_font("Arial", "B", size=14)
    pdf.cell(0, cell_height, txt=titre, ln=True, align="C")
    pdf.ln()

    # Création de l'en-tête du tableau
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(cell_width, cell_height, txt="Budgets", border=1)
    pdf.cell(cell_width, cell_height, txt="Budget quantification", border=1)
    pdf.ln()

    # Remplissage du tableau avec les données
    pdf.set_font("Arial", size=12)
    for i in range(len(modeles)):
        modele = modeles[i]
        nombre = nombres[i]
        pdf.cell(cell_width, cell_height, txt=modele, border="LBR")
        pdf.cell(cell_width, cell_height, txt=str(nombre), border="LBR")
        pdf.ln()

    # Sauvegarde du fichier PDF
    pdf.output(f"budget{str(current_date)}.pdf")

def report():
    ll = []
    kk = []
    list_histo = read()
    for i in list_histo[2:]:
        name_eco, value = i.split(':')
        ll.append(name_eco)
        kk.append(value)
    x = np.array(ll)
    y = np.array(kk)
    plt.bar(x,y)
    plt.show()
    pdf = input('would you like get a pdf as report for this month ?')
    if pdf == 'yes':
        name_current_month, current_date, current_year = time_life()
        pdf_report(current_date, ll, kk)
    

def change_element(liste):
    fichier_xml = read_data(liste)
    # Parse le fichier XML
    tree = ET.parse(fichier_xml)
    # Obtient la racine de l'arborescence XML
    root = tree.getroot()

    nb_modif = 0
    nb_modif = int(input('number of elements to change ?'))
    while nb_modif != 0:
        nb_modif -= 1
        month_year = input('''give the month and the year concerned (must be sticked together) 
        ex :June2023 and the element name you 'd like to change both have to be separated by a space''').split()
        # Trouver l'élément <renting_location>
        element_modif = root.find(f"./{month_year[0]}/{month_year[1]}")
        if element_modif is not None:
            # Modifier la valeur de l'élément
            mod_value = input('which value to modify ? ')
            element_modif.text = mod_value
            # Enregistrer les modifications dans le fichier XML
            tree.write(fichier_xml)
            print("La valeur a été modifiée avec succès.")
        else:
            print("L'élément à modifier n'a pas été trouvé.")


def simple_reading():
    try:
        contents = os.listdir('dossierxml')
        x = 0
        print('here is the budjet month list : ')
        liste = []
        for i in contents:
            x += 1
            print('Num:', x, ':', i)
            liste.append(i)
        if x == 1:
            print()
            print('there is just ' + str(x) + ' existing file')
        else:
            print()
            print('there are ' + str(x)+' existing files')
    except FileNotFoundError:
        print('Sorry no existing file')
    except Exception as e:
        print('a mistake happened here ' + str(e))
    return liste

def read_data(liste):
    which_file = int(input('which file you would like to read data?'))
    # Chemin vers le fichier XML
    fichier_xml = f"C://Users//Aquaman//dossierxml//{liste[which_file-1]}"
    return fichier_xml

def read():
    list_histo = []
    liste = simple_reading()
    fichier_xml = read_data(liste)
    # Parse le fichier XML
    tree = ET.parse(fichier_xml)
    # Obtient la racine de l'arborescence XML
    root = tree.getroot()
    # Parcours des éléments enfants de la racine
    for element in root.iter():
        # Affiche le nom de l'élément et son contenu
        print(element.tag, ":", element.text)
        list_histo.append(element.tag + ":" + str(element.text))
    print(list_histo)
    return list_histo  

def time_life():
    current_month = datetime.datetime.now().month
    name_current_month = calendar.month_name[current_month]
    current_date = datetime.date.today()
    current_year = datetime.datetime.now().year
    return name_current_month, current_date, current_year

def create_budget_month():
    paycheck = int(input('What is your paycheck? '))
    renting_location = int(input('What are your renting location incomes? '))
    renting_fees = int(input('What are your renting fees? '))
    food_expenses = int(input('What are your food expenses? '))
    electricity_invoice = int(input('What is your electricity invoice for the month? '))
    transport_expenses = int(input('What are your transport expenses? '))
    sum1 = sum([paycheck, renting_location])
    sum2 = sum([renting_fees, food_expenses, electricity_invoice, transport_expenses])
    balance = sum1 - sum2
    pp = [
        ('paycheck', paycheck),
        ('renting_location', renting_location),
        ('renting_fees', renting_fees),
        ('food_expenses', food_expenses),
        ('electricity_invoice', electricity_invoice),
        ('transport_expenses', transport_expenses),
        ('total_incomes', sum1),
        ('total_expenses', sum2),
        ('balance', balance)
    ]

    name_current_month, current_date, current_year = time_life()
    # Création du document XML
    doc = minidom.Document()
    # Création de l'élément racine
    root = doc.createElement(f"budget{current_date}")
    doc.appendChild(root)
    # Création du premier livre
    livre = doc.createElement(name_current_month + str(current_year))
    livre.setAttribute("id", '1')
    root.appendChild(livre)

    # Ajout des éléments dans le livre
    for name, value in pp:
        element = doc.createElement(name)
        element.appendChild(doc.createTextNode(str(value)))
        livre.appendChild(element)
    
    # Enregistrement du document XML dans un fichier
    with open(f"C://Users//Aquaman//dossierxml//budget{str(current_date)}.xml", "w", encoding="utf-8") as file:
        doc.writexml(file, indent="\t")
    print("Fichier XML créé avec succès.")

def main():
    if not os.path.exists("dossierxml"):
        os.makedirs("dossierxml")

    bb = ''
    while bb != 'stop':
        bb = input("""you want to 'stop', 'create' a new month budget, 'get' pdf of all caracteristics for a
                    month, 'cancel' one month, 'change' a specific information inside an xml file, 'read' a specific xml file""")
        if bb == 'create':
            create_budget_month()
        if bb == 'read':
            read()
        if bb == 'stop':
            exit(0)
        if bb == 'change':
            liste = simple_reading()
            change_element(liste)
        if bb == 'report':
            report()
main()
