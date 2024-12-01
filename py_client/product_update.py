import requests

endpoint = "http://localhost:8000/api/products/11/update/"

data = {
    "title": "John Jacobs Sunglasses",
}

# response = requests.put(endpoint, json=data)
response = requests.patch(endpoint, json=data)

print(response.json())
print(response.status_code)
