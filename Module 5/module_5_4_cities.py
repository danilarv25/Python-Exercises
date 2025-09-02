# list of cities
l_cities = []

# ask for each city name
for i in range(5):
    city = input("Enter city: ")
    l_cities.append(city)

# print all cities, one per line
for i in l_cities:
    print(i)