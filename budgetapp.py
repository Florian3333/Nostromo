import datetime
import calendar
from fpdf import FPDF
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import os
import sys
import matplotlib
import numpy as np


def addition(value1, value2, value3 = 0, value4 = 0):
    dd = value1 + value2 + value3 + value4
    return dd

def xml_creation():
    # Création de l'élément racine du fichier XML
    racine = ET.Element("budgets")

    # Création d'un élément "personne"
    personne = ET.SubElement(racine, "personne_budget")

    # Ajout d'un attribut à l'élément "personne"
    personne.set("id", now_month)

    # Ajout d'éléments enfants à l'élément "personne"
    incomes = ET.SubElement(personne, f"sum_incomes{now_month}")
    incomes.text = str(sum1)

    expenses = ET.SubElement(personne, f"sum_expenses{now_month}")
    expenses.text = str(sum2)

    deficit_exedent = ET.SubElement(personne, f"deficit_exedent{now_month}")
    deficit_exedent.text = str(total)

    # Création de l'arbre XML
    arbre_xml = ET.ElementTree(racine)
    # Enregistrement de l'arbre XML dans un fichier
    arbre_xml.write(f"budget_months{now_month}.xml")


def histogram(sum_incomes, sum_expenses, deficit_exedent):
    x = np.array(['sum incomes', "sum expenses", "total excedent ou deficit"])
    y = np.array([sum_incomes, sum_expenses, deficit_exedent])
    plt.bar(x,y)
    plt.show()

def lire_xml():
    # Charger le fichier XML existant
    arbre_xml = ET.parse(f"budget_months{now_month}.xml")
    # Obtenir la racine de l'arbre XML
    racine = arbre_xml.getroot()
    # Parcourir les éléments de la racine
    for element in racine:
        # Extraire les données des éléments enfants
        id_personne = element.get("id")
        sum_incomes = element.find(f"sum_incomes{now_month}").text
        sum_expenses = element.find(f"sum_expenses{now_month}").text
        deficit_exedent = element.find(f"deficit_exedent{now_month}").text
        
        # Afficher les données
        print("ID:", id_personne)
        print("total incomes:", sum_incomes)
        print("total expenses:", sum_expenses)
        print("deficit or exedent", deficit_exedent)
        histogram(sum_incomes, sum_expenses, deficit_exedent)
    return sum_incomes, sum_expenses, deficit_exedent

def calculation_itself(total, aa):
    if aa < 0 :
        ff = 'a deficit situation of'
    else:
        ff = 'an excedent of'
    total += aa
    print('you have' + str(ff), aa)
    return total ,aa

def budget_calculation(total):
    print('Your incomes for this month ?')
    paycheck = int(input('what is your paycheck ?'))
    renting = int(input('what is your renting location incomes ?'))

    sum1 = addition(paycheck, renting)
    print('your incomes\'s total is ', sum1)

    print('Your expenses for this month ?')
    renting_fees = int(input('what are your renting fees ?'))
    food_expenses = int(input('what is your food expenses ?'))
    electricity_invoice = int(input('what is your electricity invoice for the month ?'))
    transport_expenses = int(input('what is your transport expenses ?'))

    sum2 = addition(renting_fees, food_expenses, electricity_invoice, transport_expenses)
    print('your expenses\'s total is ', sum2)
    aa = sum1-sum2
    if aa < 0:
        total, aa =calculation_itself(total, aa)
    else:
        total, aa =calculation_itself(total, aa)
    return sum1, sum2, total

def cancel_xml():
    chemin_fichier = f"C://Users//Aquaman//budget_months{now_month}.xml"
    os.remove(chemin_fichier)

def creation_pdf():
    current_date = datetime.date.today()
    # Création d'une classe PDF personnalisée en héritant de FPDF
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, f'budget calculated during the {current_date}', align='C', ln=True)

        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

        def chapter_title(self, num, title):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, f'budget calculated during the {current_date}', ln=True)

        def chapter_body(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 10, body)
            self.ln()

    # Création d'une instance de la classe PDF
    pdf = PDF()

    # Ajout des pages
    pdf.add_page()

    # Ajout du titre et du corps du chapitre
    pdf.chapter_title(1, f'statistics budget for the {current_date}')
    pdf.chapter_body('sum of your incomes : '+ str(sum_incomes) + ' sum of your expenses : ' + str(sum_expenses) + ' sum of your exedent or deficit : ' + str(deficit_exedent))
    # Enregistrement du fichier PDF
    pdf.output(f'exemple{current_date}.pdf')



now_month = ''
current_month = datetime.datetime.now().month
name_current_month = calendar.month_name[current_month]

if now_month != name_current_month:
    now_month = name_current_month
    print('the month has changed we are now in ', now_month)
else:
    print("we are in ", now_month)

total = 0
stop = ''
while stop != 'stop':
    stop = input('do you wish to stop or continue or statistic ?')
    if stop == "continue":
        if not os.path.exists(f"budget_months{now_month}.xml"):
            sum1, sum2, total = budget_calculation(total)
            cancel_xml()
            xml_creation()
        else:
            sum1, sum2, total = budget_calculation(total)
            xml_creation()

    if stop == "statistic":
        sum_incomes, sum_expenses, deficit_exedent = lire_xml()
        creation_pdf()
