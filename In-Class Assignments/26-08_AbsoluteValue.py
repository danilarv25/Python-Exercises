num = int(input("Please give a number: "))

if num < 0:
    absval = num*-1
    print("The absolute value of this number is "+str(absval))
else:
    print("The absolute value of this number is "+str(num))