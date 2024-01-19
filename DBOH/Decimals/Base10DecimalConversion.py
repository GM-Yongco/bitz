print("~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")
import math

def convert(Converteee, Base):
    q = Converteee
    f = 0
    a = ""

    NinePlus = ['a','b','c','d','e','f']

    for i in range (20):
        q = q * Base
        f = math.floor(q)
        q = q - f

        # below converts the things for hexadecimal
        if(f>9):
            Fconvert = NinePlus[int(f)-10]
        else:    
            Fconvert = str(f)
        a = a + Fconvert
    print(f"0." + a)

n = float(input("Base 10 Decimal to be converted: "))
base = float(input("Base to be converted to: "))

if(n>=1):
    # connverts base 10 numbers below 0 to their different number systems
    print("foolish fool, only decimals")
    exit()
    print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")
else:
    convert(n,base)



print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")
