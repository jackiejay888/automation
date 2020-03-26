OpenLoop=false
Test_res=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="CAMERA"
project_name="USC130_A8"
log_patch="/data/testtool"

echo 'MSG:'
echo 'Test_Item: CAMERA hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: CAMERA hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

lsusb | grep 2394
lsusb | grep 2394 >> $log_patch/$project_name"_"$fun"_"$now.log &


#CAMERA=`cat /sys/devices/platform/ff500000.usb/usb2/2-1/2-1.1//2-1.1:1.0/input/input1/name`
CAMERA=`cat /sys/class/video4linux/video0/name`
echo $CAMERA >> $log_patch/$project_name"_"$fun"_"$now.log &

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

echo 'Result:' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
if [ "$Test_res" == "true" ] ; then
   echo 'PASS' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
   echo 'FAIL' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
fi
echo 'Result end' >> $log_patch/$project_name"_"$fun"_"$now.log &

