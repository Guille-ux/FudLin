mkdir output
mkdir payloads
mkdir nshell
mv nshell.py nshell
mv nbot.py payloads
mv bashloader.py payloads
cd ..
hast='pwd'
cd
echo alias 'fudlin'='python3 $hastFudLin' >> .bashrc
