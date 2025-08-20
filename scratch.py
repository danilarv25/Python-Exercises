numlist = []
turns = 0
while turns < 3:
    num = int(input("Please give a number: "))
    numlist.append(num)
    turns += 1

sum = 0
for i in numlist:
    sum += i
print("The sum of "+str(numlist)+" is: "+str(sum))

prod = numlist[0]
prod = int(prod)
for i in numlist:
    if i == numlist[0]:
        pass
    else:
        prod = prod*i
print("While the product is: "+str(prod))

avrg = prod / turns
print("And the average of the numbers is: "+str(avrg))