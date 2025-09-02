groceries = ["milk", "butter", "bread"]

bought = input("Item purchased: ").lower()

# keep asking as long as input is NOT empty
while (bought != "" and len(groceries) != 0):
    # if input is found in list, remove it and print the remainder
    if bought in groceries:
        groceries.remove(bought)
        print(f"Items remaining: {groceries}")
    # if input is NOT in list, notify user
    else:
        print(f"{bought} is not on the list!")
        print(f"Items remaining: {groceries}")
    if len(groceries) > 0:
        bought = input("Item purchased: ")
# if the list is empty once the loop finishes, congratulate
# otherwise, print remainder
if len(groceries) == 0:
    print("Groceries list empty!")
else:
    print(f"Groceries left for next time: {groceries}")
