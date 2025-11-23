from helper import som
from presentatie import *
import csv

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade_ijs-totaal" : 1500,
    "water_ijs-totaal" : 750
}

totaal_inkomsten = som(inkomsten)

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=':')
        writer.writerow([key, value])
        presenteer(inkomsten, totaal_inkomsten)
