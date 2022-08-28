mkdir output
mkdir payloads
mkdir nshell
mv nshell.py nshell
mv nbot.py payloads
mv bashloader.py payloads
cd ..
hast='pwd'
cd
echo hast=$hast; alias 'fudlin'='cd $hast; python3 FudLin.py' >> .bashrc
