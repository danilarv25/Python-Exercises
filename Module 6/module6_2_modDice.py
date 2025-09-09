import random
def diceRoll(sides):
    cast = random.randint(1, sides)
    return cast
x = int(input("Give how many sides"))
cast = 0
while cast != x:
    cast = diceRoll(x)
    print(cast)