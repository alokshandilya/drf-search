import requests

endpoint = "https://api.github.com/users/alokshandilya"

response = requests.get(endpoint)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dictionary

print("response.json() : ", response.json(), end="\n\n")
print("response.status_code : ", response.status_code, end="\n\n")
# print(response.text") # HTML response as text unicode
print("response.url : ", response.url, end="\n\n")
print("response.request : ", response.request)
