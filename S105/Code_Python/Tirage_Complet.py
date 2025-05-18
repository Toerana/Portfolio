from Tirage_Loto import *
from CSV_Data import *
from JSON_Data import *
from Binaire_Data import *
from Histogramme import *

israndom = input("Tirage avec seed spécifique ? oui/non : ")
nbtirage = int(input("Entrer le nombre de tirage voulu : "))

data = []

if israndom == "oui":
    seed = int(input("Définisser la seed : "))
    for i in range(nbtirage):
        data.append(Tirage(seed))
else:
    seed = 0

for i in range(nbtirage):
    data.append(Tirage(seed))
    seed += 1

save = input("Vouler vous sauvegarder les tirage ? oui/non : ")
if save == "oui":
    save_format = input("Enter le format de fichier binaire/csv/json : ")
    if save_format == "binaire":
        binaire_write(data,"Data/data_binaire.bin")
    elif save_format == "csv":
        csv_write(data,"Data/data_csv.csv")
    elif save_format == "json":
        json_write(data,"Data/data_json.json")

histo = input("Vouler vous un histogramme ? oui/non : ")
if histo == "oui":
    histograme(data)
