length = float(input("Please give the length and width of a rectangle, starting with the length: "))
width = float(input("And now the width, please: "))
area = length*width
perim = (length*2) + (width*2)
print("With a length of "+str(length)+" units and a width of "+str(width)+" units, the area is: "+str(area)+" square units")
print("The perimeter is then: "+str(perim)+" units")