import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(
    endpoint,
    params={"product_id": 7},  # query parameters (can be placed in endpoint)
    json={"username": "aloks"},  # JSON data in body
)

print(response.json())
print(response.status_code)
