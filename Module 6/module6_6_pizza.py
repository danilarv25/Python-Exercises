import math

def value_pizza(diameter, cost):
    meters = (math.pi*((diameter/2)**2))/100
    # print(f"Area in square meters: {meters:.2f}")
    value = cost/meters
    # print(f"Value of pizza (price per square meter): {value:.2f}")
    return value

print("Let's compare pizzas!")
pizza1d = int(input("How big, in centimeters, is the first pizza? "))
pizza1c = int(input("How much, in euros, did it cost? "))
pizza2d = int(input("How big, in centimeters, is the second pizza? "))
pizza2c = int(input("How much, in euros, did it cost? "))
pizza1val = value_pizza(pizza1d, pizza1c)
pizza2val = value_pizza(pizza2d, pizza2c)
if pizza1val > pizza2val:
    print(f"The second pizza ({pizza2d} centimeters for {pizza2c} euros) offers the better value")
else:
    print(f"The first pizza ({pizza1d} centimeters for {pizza1c} euros) offers the better value")