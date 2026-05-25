import requests
from datetime import datetime

sites = [
    "https://google.com",
    "https://github.com"
]

with open("status.log", "a") as log:
    for s in sites:
        try:
            r = requests.get(s, timeout=5)
            msg = f"{datetime.now()} | {s} | {r.status_code}\n"
        except Exception as e:
            msg = f"{datetime.now()} | {s} | DOWN\n"

        print(msg.strip())
        log.write(msg)
