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
print("With a length of "+str(length)+" units and a width of "+str(width)+" units, the area is: "+str(area))
print("The perimeter is then: "+str(perim))