cabclass = input("Enter cabin class: ").lower()

if cabclass == "lux":
    print("LUX: upper-deck cabin with a balcony.")
elif cabclass == "a":
    print("A: above the car deck, equipped with a window.")
elif cabclass == "b":
    print("B: windowless cabin above the car deck.")
elif cabclass == "c":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")