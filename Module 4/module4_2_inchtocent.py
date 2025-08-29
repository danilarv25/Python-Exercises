x = float(input("Input value for inches (negative number to quit): "))

while x > 0:
    c = x*2.54
    print(f"{x} inches is equal to {c} centimeters")
    x = float(input("Input value for inches (negative number to quit): "))

print("Goodbye!")