soupcost = 5.90
customer = input("Please tell me your name: ")

if customer.lower() == "matti":
    print("Next please!")
else:
    portions = int(input("How many portions of soup? "))
    print(f"The total cost is {(soupcost*portions):.2f}")
    print("Next please!")