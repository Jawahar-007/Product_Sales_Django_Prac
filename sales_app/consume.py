import requests

response = requests.get('http://localhost:8000/products/')
print(response.json())  # Output: {'products': []}