# Description     : binary conversion using string comparisons; its seriously so sketchy
# Author          : NxM Jules
# Date            :
# ~~~~~~~~~~~~~~~~~~~HEAD~~~~~~~~~~~~~~~~~~~
import math
# ~~~~~~~~~~~~~~GlobalVariables~~~~~~~~~~~~~
inspo1 = "Do things that make you love yourself :DDD"
inspo2 = "Be someone who can stand by Shinomiya"
inspo3 = "PLUS ULTRAAA"

baseNDict   = {8:3, 16:4}

octalDict   = {'001': 1, '010': 2, '011': 3,'100': 4,'101': 5, '110': 6, '111': 7}
hexDict     = {"0001": 1, "0010": 2, "0011": 3, "0100": 4, "0101": 5,"0110": 6, "0111": 7, "1000": 8,
             "1001": 9, "1010": 'a', "1011": 'b',"1100": 'c', "1101": 'd', "1110": 'e', "1111": 'f',}

conNDict    = {8: octalDict, 16:hexDict}

print("~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~\n")

# INPUT~~~~~~~~~~~~~~~~~~~~~~~~~~~

base2var = input("Base 2 to be converted: ")
baseNew = int(input("Base to be converted to: "))
# note: this only works on base 8 and base 16 


# FORMATTING~~~~~~~~~~~~~~~~~~~~~~~~~~~

baseN = baseNDict[baseNew]

if (len(base2var) % baseN) != 0:
    for i in range (baseN - (len(base2var) % baseN)):
        base2var = "0" + base2var
# the lenght of base2var should now be divisible by BaseN
# basically turns a "1" into a "001" for base 8 conversion or a "0001" for base 16 conversion


# CONVERSION~~~~~~~~~~~~~~~~~~~~~~~~~~~

bNvar = ""       # short for New Base Variable
b2con = ""       # short for Base 2 convert

for i in range (int((len(base2var)) /baseN)):
    b2con = base2var[-baseN:]   #gets the last 3 or 4 digits depending on the base
    base2var = base2var[:-baseN]#sets the original variable to itself without the last digits

    bNvar = str(conNDict[baseNew][b2con]) + bNvar
    # "conNDict[baseNew]" uses a dictionary to determine which dictionary to use
    # "the dictionary used will convert the string to their equivalent"
    # "then string concatenate the it to the most left of the string"

print(bNvar)

print("\n~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")
