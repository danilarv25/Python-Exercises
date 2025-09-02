numlist = []
nlordered = []
x = int(input("Give number: "))

while x != 0:
    nlordered = []
    numlist.append(x)
    nlordered.extend(numlist)
    nlordered.sort()
    print(f"The list now: {numlist}")
    print(f"The list in order: {nlordered}")
    x = int(input("Give number: "))

print("Bye!")