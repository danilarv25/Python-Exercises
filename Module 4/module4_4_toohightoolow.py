import random
print("")
num = random.randint(1,10)
guess = 0
while guess != num:
    guess = int(input("Guess the number: "))
    if guess == num:
        print("Correct!")
        break
    elif guess < num:
        print("Too low!")
        # print(num)
    elif guess > num:
        print("Too high!")
        # print(num)
