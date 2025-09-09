season = ("spring", "summer", "autumn", "winter")

x = int(input("Month's number to check: "))

if (x==12 or 1 <= x <= 2):
    print(season[3])
elif 3<=x<=5:
    print(season[0])
elif 6<=x<=8:
    print(season[1])
elif 9<=x<=11:
    print(season[2])