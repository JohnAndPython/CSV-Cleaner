#********************#
# Main Programm
#********************#


import os
import csv

path_of_main = os.path.dirname(os.path.abspath(__file__))

#Create necessary folders, if they do not exist
try:
    os.mkdir(path_of_main + "\\Template")
except FileExistsError:
    None

try:
    os.mkdir(path_of_main + "\\Erorrprotokoll")
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
