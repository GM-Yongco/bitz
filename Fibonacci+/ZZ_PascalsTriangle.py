print("~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

from array import *

NPL = input("nth Pascal's Triangle Layer: ")
PL1 = array('i',(0,1,0))
PL2 = array('i',(0,1,1,0))
PL3 = array('i',())

print(PL1)
print(PL2)

for d in range (int(NPL)):
    PL3 = array('i',())
    PL3.append(0)
    c = 0
    while c==c:
        PL3.append(PL2[c]+PL2[c+1])
        c += 1
        if len(PL3) == len(PL2):
            break
    PL3.append(0)
    print(PL3)

    PL2 = PL3

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~")
