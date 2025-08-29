low = 0
high = 0
while True:
    x = input("Enter a number (string to quit): ")
    if x.isdigit():
        x = int(x)
        if low == 0 and high == 0:
            high = low = x
        elif x < low:
            low = x
        elif x > high:
            high = x
    else:
        print(f"Lowest number: {low}    Highest number: {high}")
        print("Goodbye!")
        break