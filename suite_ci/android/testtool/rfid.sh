OpenLoop=false
Test_res=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="rfid"
project_name="usc130_a8"
cpu="rk3288"
android_version="a8"
log_patch="/data/testtool"

#check support cpu
if [ -n "$1" ] ; then

cpu=$1
#echo $project_name

else
cpu="rk3288"
#echo $project_name
fi

if [ "$cpu" == "rk3288" ] ; then
  echo 'rk3288'
else
if [ "$cpu" == "imx6" ] ; then
   echo 'imx6'
else
   echo 'Not support cpu'
   exit 0
fi 
fi
#check support cpu

#check support android_version
if [ -n "$2" ] ; then

android_version=$2
#echo $project_name

else
android_version="a8"
#echo $project_name
fi

if [ "$android_version" == "a8" ] ; then
  echo 'a8'
else
if [ "$android_version" == "a6" ] ; then
   echo 'a6'
else
   echo 'Not support cpu'
   exit 0
fi 
fi
#check support android_version

#check support device
if [ -n "$3" ] ; then

project_name=$3
#echo $project_name

else
project_name="usc130_a8"
#echo $project_name
fi

#check support device

echo 'MSG:'
echo 'Test_Item: rfid hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: rfid hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

#lsusb | grep 10c4
lsusb | grep $4
#RFID = 'ls /dev/ttyUSB2'
#RFID=`ls /dev/ttyUSB2 | busybox awk '{print substr($0,1)}'`
RFID=`ls $5 | busybox awk '{print substr($0,1)}'`
echo $RFID
echo $RFID >> $log_patch/$project_name"_"$fun"_"$now.log &

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

