numlist = []

while True:
    x = input("Add a number (empty string to quit): ")
    if x.isdigit():
        numlist.append(int(x))
    else:
        break

ognumlist = []
ognumlist.extend(numlist)
numlist.sort(reverse=True)
print(numlist[0:5])