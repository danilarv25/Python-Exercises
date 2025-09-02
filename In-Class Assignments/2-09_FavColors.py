colors = ["yellow", "green", "blue", "violet", "red", "orange"]

fav = input("Enter favorite color: ").lower()
if fav in colors:
    print(f"{fav} is on the list!")
elif fav == "purple":
    print(f"{fav} isn't on the list, but violet is!")
else:
    print(f"{fav} is not on the list!")