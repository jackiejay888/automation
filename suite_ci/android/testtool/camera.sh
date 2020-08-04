OpenLoop=false
Test_res=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="camera"
#project_name="usc130_a8"
project_name=`getprop ro.build.product`
#cpu="rk3288"
cpu=`getprop ro.board.platform`
#android_version="a8"
android_version=`getprop ro.build.version.release`
log_patch="/data/testtool"

#check support cpu

if [ "$cpu" == "rk3288" ] ; then
  echo 'rk3288'
else
if [ "$cpu" == "imx6" ] ; then
   echo 'imx6'
else
if [ "$cpu" == "gmin" ] ; then
   echo 'gmin'
else
   echo $cpu
#   exit 0
fi 
fi 
fi
#check support cpu

#check support android_version

if [ "$android_version" == "8.1.0" ] ; then
  echo '8.1.0'
else
if [ "$android_version" == "6.0.0" ] ; then
   echo '6.0.0'
else
if [ "$android_version" == "6.0.1" ] ; then
   echo '6.0.1'
else
   echo $android_version
#   exit 0
fi
fi 
fi
#check support android_version


#check support device

#check support device

echo 'MSG:'
echo 'Test_Item: camera hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: camera hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &


if [ "$1" == "adv7180" ] ; then
echo adv7180
echo adv7180 >> $log_patch/$project_name"_"$fun"_"$now.log &
else
if [ "$1" == "ATOMISP" ] ; then
echo ATOMISP
echo ATOMISP >> $log_patch/$project_name"_"$fun"_"$now.log &
else
if [ "$1" == "2394" ] ; then
lsusb | grep 2394
lsusb | grep 2394 >> $log_patch/$project_name"_"$fun"_"$now.log &
else
if [ "$1" == "msm-sensor" ] ; then
echo msm-sensor
echo msm-sensor >> $log_patch/$project_name"_"$fun"_"$now.log &

fi

fi
fi 
fi

#CAMERA=`cat /sys/devices/platform/ff500000.usb/usb2/2-1/2-1.1//2-1.1:1.0/input/input1/name`
CAMERA=`cat /sys/class/video4linux/video0/name`
echo $CAMERA
echo $CAMERA >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ "$1" == "msm-sensor" ] ; then
CAMERA2=`cat /sys/class/video4linux/video3/name | /data/testtool/busybox awk '{print $1}' `
else
CAMERA2=`cat /sys/class/video4linux/video0/name | /data/testtool/busybox awk '{print $1}' `
fi
#echo $CAMERA2

if [ "$1" != "$CAMERA2" ] ; then
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

