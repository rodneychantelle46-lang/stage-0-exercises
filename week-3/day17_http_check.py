import requests
url = 'https://example.com'
response = requests.get(url,timeout=10)

print('status:', response.status_code)
print('preview:', response.text[:80])