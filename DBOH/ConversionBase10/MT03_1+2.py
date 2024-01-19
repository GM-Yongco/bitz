# Description     : outputs the full first digit multiplication table in the respective base's format
# Author          : NxM Jules
# Date            : 
# ~~~~~~~~~~~~~~~~~~~HEAD~~~~~~~~~~~~~~~~~~~

print("~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

def converter(Base10, Base):
    Q = int(Base10)
    B = int(Base)

    NinePlus = ['a','b','c','d','e','f']

    R = 1
    O = ""
    # doesnt do anything specific, just initialization

    while (Q!=0):
        R = Q%B
        Q = int(Q/B)
        if (R>9):
            O = NinePlus[R-10] + O
        else:
            O = str(R) + O

    return(O)

print("~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~")

n = int(input("Base multiplication table: "))

for i1 in range(1,n):
    for i2 in range(1,n):
        i3 = i1 * i2
        print(f"" + str(converter(i1,n)) + " x " + str(converter(i2,n)) + " = " + str(converter(i3,n)))
    print("~~~~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")
