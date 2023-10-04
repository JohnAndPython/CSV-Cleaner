#********************#
# Main Programm
#********************#


import os
import csv
import create_files

path_of_main = os.path.dirname(os.path.abspath(__file__))

#Create necessary folders, if they do not exist
try:
    os.mkdir(path_of_main + "\\Template")
except FileExistsError:
    None

try:
    os.mkdir(path_of_main + "\\Erorrprotocol")
except FileExistsError:
    None

try:
    os.mkdir(path_of_main + "\\Offers")
except FileExistsError:
    None

try:
    os.mkdir(path_of_main + "\\Cleaned")
except FileExistsError:
    None

#Get path of directorys
template_path = path_of_main + "\\Template"
errorProtocol_path = path_of_main + "\\Erorrprotocol"
offer_path = path_of_main + "\\Offers"
cleared_path = path_of_main + "\\Cleaned"

#check if all necessary files exist, if not create them
if os.path.isfile(template_path + "\\SpecialCode.csv") == False:
    create_files.create_file_EF(template_path + "\\SpecialCode.csv")

if os.path.isfile(template_path + "\\RealCSV.csv") == False:
    create_files.create_file_RCSV(template_path + "\\RealCSV.csv")

if os.path.isfile(template_path + "\\KeyValue_Column_1.csv") == False:
    create_files.create_file_KEYCSV(template_path + "\\KeyValue_Column_1.csv")

#store all csv-files in the Directory Offers in a list
allCSVFiles_list = [CSVfile for CSVfile in os.listdir(offer_path) if CSVfile.lower().endswith(".csv")]

#Open special code Template and store the content in a list
templspecialcode = list()

try:
    with open(template_path + "\\SpecialCode.csv", "r", newline="") as input_specialcodef:
        reader_specialcodef = csv.reader(input_specialcodef, delimiter=";")
        
        templspecialcode = list(reader_reader_specialcodef)[0]
except:
        print("File SpecialCode cannot be opend")





