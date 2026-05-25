import os

print("CPU INFO")
os.system("cat /proc/cpuinfo | head")

print("\nMEMORY")
os.system("free -h")
