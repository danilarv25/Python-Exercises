user = "python"
passw = "rules"
t = 0
while t < 5:
    namein = input("Enter username: ")
    passin = input("Enter password: ")
    if (namein == user and passin == passw):
        print("Welcome")
        break
    else:
        if t < 4:
            print(f"Either your username or password is incorrect. Please try again. ({4-t} tries left)")
        else:
            print("Either your username or password is incorrect.")
    t += 1

if t == 5:
    print("Access denied")
    quit()