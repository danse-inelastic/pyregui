echo ">> The following command should prompt user to use wxpyregui.py -h"
echo wxpyregui.py 
echo Press ENTER to continue
read 
wxpyregui.py 

#echo
#echo
#echo ">> The following command should print out a simple help"
#echo wxpyregui.py -h
#echo Press ENTER to continue
#read 
#wxpyregui.py -h


echo
echo
echo ">> The following command should complain that it cannot find the application "
echo wxpyregui.py abcdefghijkhello
echo Press ENTER to continue
read 
wxpyregui.py abcdefghijkhello

echo
echo
echo ">> The following command should bring up a gui for simple.py"
echo wxpyregui.py simple.py
echo Press ENTER to continue
read
wxpyregui.py simple.py



