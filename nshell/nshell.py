import os, sys, time

print("press ctrl + c to quit")
port = input("Port: ")
os.system("python3 -m http.server {} > /dev/null 2>&1 &".format(port))
while True:
    try:
        com = input("$ ")
        os.system(f"echo '{com}' > data.sh")
        time.sleep(1)
        os.system("echo ' ' > data.sh")
    except KeyboardInterrupt:
        sys.exit()
