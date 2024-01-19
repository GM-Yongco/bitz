# Description     : Makes the covertion table up to n
# Author          : NxM Jules
# Date            : ur my date uwu
# ~~~~~~~~~~~~~~~~~~~HEAD~~~~~~~~~~~~~~~~~~~
print("~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

N = int(input("nth Convertion: "))

D = 1

while(D<(N+1)):
    # initializtion of variables
    Q = D
    R = 1
    B = ""

    # binary
    while (Q!=0):

        R = Q%2
        Q = int(Q/2)
        
        B = str(R) + B
    # octal
    Q = D
    R = 1
    O = ""
    while (Q!=0):

        R = Q%8
        Q = int(Q/8)
        
        O = str(R) + O
    # hex
    Q = D
    R = 1
    H = ""

    hex = ['a','b','c','d','e','f']

    while (Q!=0):

        R = Q%16
        Q = int(Q/16)
        if(R>9):
            T = hex[R-10]
        else:    
            T = str(R)
        H = T + H

    # printing
    # just some spacing for neatness
    if(len(B)>7):
        print(f""+ str(D) + "\t\t" + str(B) + "\t" + str (O) + "\t\t" + str(H))
    else:
        print(f""+ str(D) + "\t\t" + str(B) + "\t\t" + str (O) + "\t\t" + str(H))
    
    # loop update
    D = D + 1

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~")
