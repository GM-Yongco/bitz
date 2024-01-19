
# Description     : binary conversion using string comparisons; its seriously so sketchy
# Author          : NxM Jules
# Date            :
# Header~~~~~~~~~~~~~~~~~~~
import math
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GLOBAL VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BtLDict = {8:3, 16:4}
# binary to length
BtODict = {'000': 0, '001': 1, '010': 2, '011': 3,'100': 4,'101': 5, '110': 6, '111': 7}
OtBDictIn = {v: k for k, v in BtODict.items()}     #https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
# binary & octal

BtHDict = {'0000': 0,"0001": 1, "0010": 2, "0011": 3, "0100": 4, "0101": 5,"0110": 6, "0111": 7, "1000": 8, "1001": 9, "1010": 'a', "1011": 'b',"1100": 'c', "1101": 'd', "1110": 'e', "1111": 'f',}
HtBDictIn = {v: k for k, v in BtHDict.items()} 
# binary & hex

BBDict  = {8: BtODict, 16:BtHDict}
# binary base to dictionary

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CUSTOM FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def Convert2_816(xv, yb):   
    # short for xVariable and yVariable

    BL = BtLDict[yb]
    # short for base length

    if (len(xv) % BL) != 0:
        for i in range (BL - (len(xv) % BL)):
            xv = "0" + xv
    # the lenght of base2var should now be divisible by BaseN
    # basically turns a "1" into a "001" for base 8 conversion or a "0001" for base 16 conversion

    xt = ""     # xTemp
    yv = ""     # short for yVariable

    for i in range (int((len(xv)) /BL)):
        xt = xv[-BL:]           #gets the last 3 or 4 digits depending on the base
        xv = xv[:-BL]           #sets the original variable to itself without the last digits

        yv = str(BBDict[yb][xt]) + yv
        # "BBDict[yb]" uses a dictionary to determine which dictionary to use
        # "the dictionary used will convert the string to their equivalent"
        # "then string concatenate the it to the most left of the string"

    return yv  # returs the y variable

def Convert2_10(xv, yb):
    print("hey there")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~\n")

# INPUT~~~~~~~~~~~~~~~~~~~~~~~~~~~
xBase   = int(input("Base to be converted from\t(int): "))
xVar    = input("Base " + str(xBase) + " variable to convert\t     : ")
yBase   = int(input("Base to be converted to\t\t(int): "))
yVar    = ""

# CONVERSION~~~~~~~~~~~~~~~~~~~~~~~~~~~

if (xBase == 2 and (yBase == 8 or yBase == 16)):
    print("Base " + str(yBase) + " version of the variable       : "+ str(Convert2_816(xVar, yBase)))

print("\n~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")