print("~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

def converter(Decimal, Base):
    Q = int(Decimal)
    B = int(Base)

    NinePlus = ['a','b','c','d','e','f']

    R = 1
    O = ""
    while (Q!=0):
        R = Q%B
        Q = int(Q/B)
        if (R>9):
            O = NinePlus[R-10] + O
        else:
            O = str(R) + O

    return(O)

deci = int(input("Base 10 to be converted: "))
base = int(input("Base to be converted to: "))

print(converter(deci,base))

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~")
