import random
num3 = ""
num4 = ""
for i in range(3):
    x = random.randint(0,9)
    num3 = num3+str(x)
for i in range(4):
    x=random.randint(1,6)
    num4 = num4+str(x)
print(f"3-digit code is: {num3}")
print(f"4-digit code is: {num4}")
