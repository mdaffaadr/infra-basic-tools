import socket

host = "google.com"
ports = [80, 443]

for p in ports:
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect((host, p))
        print(f"{host}:{p} OPEN")
    except:
        print(f"{host}:{p} CLOSED")
    s.close()
