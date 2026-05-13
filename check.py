import requests

sites = [
    "https://google.com",
    "https://github.com"
]

for s in sites:
    try:
        r = requests.get(s, timeout=5)
        print(f"{s} -> {r.status_code}")
    except Exception as e:
        print(f"{s} -> DOWN")
