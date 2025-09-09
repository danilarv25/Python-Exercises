import random
def diceRoll():
    cast = random.randint(1,6)
    return cast
roll = 0
while roll != 6:
    roll = diceRoll()
    print(roll)