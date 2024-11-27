import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Scissor",
    "content": "A pair of scissors",
    "price": 120.00,
}

response = requests.post(endpoint, json=data)

print(response.json())
print(response.status_code)
