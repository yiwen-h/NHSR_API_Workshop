import requests


### CAT FACTS
url = "https://meowfacts.herokuapp.com/"
response = requests.get(url)

print(response)
print(response.json())

### CAT FACTS WITH PARAMS
# url = "https://meowfacts.herokuapp.com/"
# my_params = {"count": 3, "lang": "ukr"}

# response = requests.get(url, params = my_params)
# print(response.json())

### CODING TOGETHER: HOURLY TEMPERATURE AND HUMIDITY IN KUALA LUMPUR
# url = ""
# my_params = {}

# response = requests.get(url, params = my_params)
# print(response.json())