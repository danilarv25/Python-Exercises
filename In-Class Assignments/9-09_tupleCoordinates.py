import math
def swap_coordinates(point):
    (first, second) = point
    return (second, first)

def dist_coordinates(orgpoint, newpoint):
    xDif = newpoint[0] - orgpoint[0]
    yDif = newpoint[1] - orgpoint[1]
    distance = math.sqrt((xDif**2) + (yDif**2))
    return distance

x = int(input("Give int for x-coordinate: "))
y = int(input("Give int for y-coordinate: "))
point = (x, y)
newpoint = swap_coordinates(point)
dist = round(dist_coordinates(point, newpoint), 2)

print(newpoint)
print(dist)