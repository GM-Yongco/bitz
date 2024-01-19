print("~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~")

n = int(input("Base multiplication table: "))

for i1 in range(1,n):
    for i2 in range(1,n):
        i3 = i1 * i2
        print(f"" + str(i1) + " x " + str(i2) + " = " + str(i3))
    print("~~~~~~~~~~~~~~~~~~~~")

print("~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")
