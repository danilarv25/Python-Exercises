airports = {"EFHK":"Helsinki-Vantaa Airport",
            "EBAW":"Antwerp International Airport",
            "EDDF":"Frankfurt International Airport"}

def get_airport_by_name(icao):
    ap_name = airports[icao]
    return ap_name

def update_new_airport(icao, airport_name):
    airports[icao] = airport_name
    print(f"{airport_name} has been stored under ICAO code: {icao}")
    return

while True:
    print(f"(1) Fetch an airport")
    print(f"(2) Update the database with a new airport")
    print(f"(3) View airport data")
    print(f"(4) Quit")
    action = int(input("Enter an action's number: "))

    if action == 1:
        print("")
        icao = input("Enter the airport's ICAO code\n"
                     "(enter empty string to go back): ")
        if len(icao) > 0:
            print(f"That code belongs to: {get_airport_by_name(icao)}")

    elif action == 2:
        print("\nEnter the new airport's ICAO code")
        icao = input("(enter empty string to go back): ")
        if len(icao) > 0:
            print("\nEnter the new airport's name")
            ap_name = input("(enter empty string to go back): ")
            if len(ap_name) > 0:
                update_new_airport(icao, ap_name)

    elif action == 3:
        print("")
        for i in airports:
            print(f"{i} : {airports[i]}")

    elif action == 4:
        print("\nGoodbye!")
        break