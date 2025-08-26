length = float(input("How long is the zander (centimeters)? "))
if length >= 42:
    print("You can keep the fish!")
else:
    print(f"Release it. It is {42-length} centimeters below the necessary length.")