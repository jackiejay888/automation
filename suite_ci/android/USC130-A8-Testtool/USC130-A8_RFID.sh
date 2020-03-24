OpenLoop=false
Test_res=true

echo 'MSG:'
echo 'Test_Item: RFID hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

lsusb | grep 10c4
#RFID = 'ls /dev/ttyUSB2'
RFID=`ls /dev/ttyUSB2 | busybox awk '{print substr($0,1)}'`
echo $RFID

if [ -z $RFID ] ; then
Test_res=false
fi

echo 'Result:'
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish'
else
if [ "$Test_res" == "true" ] ; then
   echo 'PASS'
else
   echo 'FAIL'
fi 
fi
echo 'Result end'
