OpenLoop=false
Test_res=true

echo 'MSG:'
echo 'Test_Item: CAMERA hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

lsusb | grep 2394

#CAMERA=`cat /sys/devices/platform/ff500000.usb/usb2/2-1/2-1.1//2-1.1:1.0/input/input1/name`
CAMERA=`cat /sys/class/video4linux/video0/name`
echo $CAMERA

CAMERA2=`cat /sys/class/video4linux/video0/name | busybox awk '{print $1}' `
#echo $CAMERA2

if [ -z $CAMERA2 ] ; then
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
