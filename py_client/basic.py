import requests

endpoint = "http://localhost:8000/api/"

# GET request
# response = requests.get(endpoint)

# POST request
response = requests.post(
    endpoint,
    # JSON data in body
    json={
        "title": "SmartPhone, Asus X00TD",
        "price": 5000,
        "content": "Asus Zenfone Max Pro M1 second hand",
    },
)

print(response.json())
print(response.status_code)
