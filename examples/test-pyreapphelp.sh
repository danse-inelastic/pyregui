echo ">> The following command should prompt user to use pyreapphelp.py -h"
echo pyreapphelp.py 
echo Press ENTER to continue
read 
pyreapphelp.py 

echo
echo
echo ">> The following command should print out a simple help"
echo pyreapphelp.py -h
echo Press ENTER to continue
read 
pyreapphelp.py -h


echo
echo
echo ">> The following command should complain that it cannot find the application "
echo pyreapphelp.py -a abcdefghijkhello
echo Press ENTER to continue
read 
pyreapphelp.py -a abcdefghijkhello

echo
echo
echo ">> The following command should print out a help page for simple.py"
echo pyreapphelp.py -a simple.py
echo Press ENTER to continue
read
pyreapphelp.py -a simple.py



