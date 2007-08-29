echo ">> The following command should prompt user to use text2pyreui.py -h"
echo text2pyreui.py 
echo Press ENTER to continue
read 
text2pyreui.py 

#echo
#echo
#echo ">> The following command should print out a simple help"
#echo text2pyreui.py -h
#echo Press ENTER to continue
#read 
#text2pyreui.py -h


echo
echo
echo ">> The following command should complain that it cannot find the application "
echo text2pyreui.py abcdefghijkhello
echo Press ENTER to continue
read 
text2pyreui.py abcdefghijkhello

echo
echo
echo ">> The following command should bring up a gui for simple.py"
echo text2pyreui.py simple.py
echo Press ENTER to continue
read
text2pyreui.py simple.py



