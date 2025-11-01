import requests, json

apikey = ""

city = input("Enter city name: ")

citycall = "http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit=1&appid="+apikey

try:
    citydata = requests.get(citycall).json()
    latitude = citydata[0]["lat"]
    longitude = citydata[0]["lon"]

except requests.exceptions.RequestException as e:
    print("Request could not be made with that name.")

print("\nLocating city...")
weathercall = "https://api.openweathermap.org/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)+"&appid="+apikey

try:
    weather = requests.get(weathercall).json()
    condition = weather["weather"][0]["description"]
    temperature = int(float(weather["main"]["temp"]) - 273.15)


except requests.exceptions.RequestException as e:
    print("There was an error fetching the weather.")

print(f"""
The weather in {citydata[0]["name"]} is...
    {condition}
    {temperature} C
""")
import requests, json

apikey = ""

city = input("Enter city name: ")

citycall = "http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit=1&appid="+apikey

try:
    citydata = requests.get(citycall).json()
    latitude = citydata[0]["lat"]
    longitude = citydata[0]["lon"]

except requests.exceptions.RequestException as e:
    print("Request could not be made with that name.")

print("\nLocating city...")
weathercall = "https://api.openweathermap.org/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)+"&appid="+apikey

try:
    weather = requests.get(weathercall).json()
    condition = weather["weather"][0]["description"]
    temperature = int(float(weather["main"]["temp"]) - 273.15)


except requests.exceptions.RequestException as e:
    print("There was an error fetching the weather.")

print(f"""
The weather in {citydata[0]["name"]} is...
    {condition}
    {temperature} C
""")