hrwage = float(input("Hourly wage: "))
hrs = float(input("Hours worked: "))
day = input("Day of the week: ").lower()
if day != "sunday":
    wageday = hrwage*hrs
    print(f"Daily wages: {wageday:.2f} euros")
else:
    wageday = 2*(hrwage*hrs)
    print(f"Daily wages: {wageday:.2f} euros")

    print(f"{day}'s wages: {wageday:.2f} euros")