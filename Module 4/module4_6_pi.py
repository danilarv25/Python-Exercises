import random
N = int(input("Enter number of dots: "))
n = 0
for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if ((x ** 2)+(y ** 2)<1):
        n += 1
piprox = (n*4)/N
print(f"The approximate value of pi is {piprox}")