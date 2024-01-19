print("~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

from array import *
NPL = input("nth Pascal's Triangle Layer: ")
PL1 = array('i',(0,1,0))

for d in range (int(NPL)):
    PL2 = array('i',())
    PL2.append(0)
    c = 0
    while c == c:
        PL2.append(PL1[c]+PL1[c+1])
        c += 1
        if len(PL2) == len(PL1):
            break
    PL2.append(0)
    print(PL1)
    PL1 = PL2

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~")