def gasToLiters(gallons):
    liters = gallons * 3.8
    return liters
gal = 0
while gal >= 0:
    gal = int(input("Input volume in gallons (negative # to stop): "))
    if gal < 0:
        print("Goodbye!")
    else:
        print(f"That amount of gallons is equal to {gasToLiters(gal):.2f} liters!")