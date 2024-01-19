print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
from array import *

NthPrime = input("nth Prime: ")
NP = int(NthPrime)
Primes = array('i',())
I = 2
PrimeCount = 0

while PrimeCount < NP:
    c1 = 0
    PrimeChecker = 0
    for c1 in range (len(Primes)):
        if I % Primes[c1] == 0:
            PrimeChecker += 1
    if PrimeChecker == 0:
        Primes.append(I)
        PrimeCount += 1
    I += 1
print (Primes[NP-1])

print("DONE")