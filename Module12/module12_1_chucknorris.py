import requests, json

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request).json()
    if requests.get(request).status_code == 200:
        print(response["value"])

except requests.exceptions.RequestException as e:
    print("Request could not be completed  D:")