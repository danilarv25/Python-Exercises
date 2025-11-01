import requests, json

keyword = input("Enter search term: ")

request = "https://api.tvmaze.com/search/shows?q="+keyword

try:
    response = requests.get(request).json()
    if requests.get(request).status_code == 200:
        for i in response:
            print(i["show"]["name"])
            print(f"    {i["score"]}")

except requests.exceptions.RequestException as e:
    print("Request could not be completed  D:")
# print(json.dumps(response, indent = 2))

