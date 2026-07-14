from getpass import getpass
import requests
url = "https://api.github.com/users/rodneychantelle46-lang/repos"
token = getpass('请输入Github token: ')
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(url, headers=headers, timeout=10)
repos = response.json()
if response.status_code == 200:
    for repo in repos:
        print(repo["name"])
else:
        print(response.status_code)
        print(repos['message'])
print("status:", response.status_code)
print("type:", type(repos))
print("count:", len(repos))
#print(repos)