while True:
    money = float(input("How much money you got?\n"))
    if money < 0:
        print("Negative money? What, you owe something? Pay up!")
    elif money == 0:
        print("Hah! You're broke, bud.")
    elif 0 < money < 5:
        print("Eh, not enough for a latte. Sorry, bud.")
    else:
        if money == 5:
            print("Alright! One latte coming right up!")
        elif 5 < money < 10:
            lattes = money//5
            change = money%5
            print("Alright! "+str(int(lattes))+" latte coming right up! Your change is "+str(change)+".")
        elif money >= 10:
            lattes = money//5
            change = money%5
            print("Alright! "+str(int(lattes))+" lattes coming right up! Your change is "+str(change)+".")
        break