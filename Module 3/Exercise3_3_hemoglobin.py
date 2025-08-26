biogender = input("Enter your biological gender: ").lower()
hemo = int(input("Enter your hemoglobin level (g/l): "))

if biogender == "female":
    if hemo < 117:
        print("Your hemoglobin level is low")
    elif 117 <= hemo <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif biogender == "male":
    if hemo < 134:
        print("Your hemoglobin level is low")
    elif 134 <= hemo <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("I'm very sorry, your gender input was not recognized. Please go with either 'male' or 'female.'")