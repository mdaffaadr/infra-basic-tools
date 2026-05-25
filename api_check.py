import requests

url = "https://api.github.com"

r = requests.get(url)

print(r.status_code)
print(r.json())
