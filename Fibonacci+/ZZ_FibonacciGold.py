print("~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

NthFib = input("nth Fibonacci Number: ")

f1 = 0
f2 = 1
f3 = 0
i = 0

while i < int(NthFib):
    f3 = f1 + f2
    i += 1
    if f1 != 0:
        print (f"Golden estimation " + str(i) + ": " + str(f2/f1))
    f1 = f2
    f2 = f3

print(f1)
print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~")