import requests
url = 'https://httpbin.org/json'
response = requests.get(url, timeout=10)
print('status:', response.status_code)
print('type:', type(response.json()))
data = response.json()
print('keys:', data.keys())