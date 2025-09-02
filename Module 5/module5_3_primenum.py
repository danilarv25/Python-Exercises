x = int(input("Give number (0 to quit): "))
while x != 0:
    # number to divide by
    y = 1

    # number of successful divisions
    z = 0

    # list containing successful denominators
    divs = []

    # divide x by y until y == x
    for i in range(x):
        if x % y == 0:
            z += 1
            divs.append(y)
        y += 1

    # since a prime number is only divisible by
    # 1 and itself, z should be equal to 2
    # z for 1 would be 1
    if z < 3:
        print(f"{x} is a prime number\n")
    # Besides declaring that x is not a prime number
    # provide list of the numbers x is divisible by
    else:
        print(f"{x} is NOT a prime number\n"
              f"This number is divisible by:\n"
              f"{', '.join(map(str,divs))}\n")
    x = int(input("Give number: "))

print("Goodbye!")
