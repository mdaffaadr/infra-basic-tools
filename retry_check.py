import requests
import time

url = "https://google.com"

for i in range(3):
    try:
        r = requests.get(url, timeout=5)
        print("SUCCESS", r.status_code)
        break
    except:
        print(f"Retry {i+1}")
        time.sleep(2)
