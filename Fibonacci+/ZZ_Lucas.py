print("~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

NthFib = input("nth Lucas Number: ")

f1 = 2
f2 = 1
f3 = 0
i = 0

while i < int(NthFib):
    f3 = f1 + f2
    i += 1
    print (f"F " + str(i) + " is: " + str(f2))
    f1 = f2
    f2 = f3

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~")
