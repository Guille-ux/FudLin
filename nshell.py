import os, sys

print("press ctrl + c to quit")
port = input("Port: ")
os.system("python3 -m http.server {} 2>&1 &".format(port))
while True:
    try:
	com = input("$ ")
	os.system("echo {} > data.sh")
    except KeyboardInterrupt:
	sys.exit()
