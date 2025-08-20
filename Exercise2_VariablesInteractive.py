'''Part 1'''
name = input("What is your name?\n")

print("Nice to meet you, "+name+"!")

'''Part 2'''
rad = float(input("Now please give the radius of a circle: "))
area = 3.14*rad*rad
area = str(area)
print("If the area is "+str(rad)+", the area is: "+area)

'''Part 3'''
length = float(input("Please give the length and width of a rectangle, starting with the length: "))
width = float(input("And now the width, please: "))
area = length*width
perim = (length*2) + (width*2)
print("With a length of "+str(length)+" units and a width of "+str(width)+" units, the area is: "+str(area)+" square units")
print("The perimeter is then: "+str(perim)+" units")

'''Part 4'''
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