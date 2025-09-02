import random

rolls = int(input("How many dice to roll? "))
sum = 0

for i in range(rolls):
    newroll = random.randint(1,6)
    sum += newroll
    #print(newroll)

print(f"The sum after {rolls} rolls is {sum}")