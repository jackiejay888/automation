OpenLoop=false
Test_res=true
TestMSG=""
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="usb_info"
#project_name="usc130_a8"
project_name=`getprop ro.build.product`
#echo $project_name
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
echo 'Test_Item: usb_info'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: usb_info hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ -n  "$1" ] ; then

/data/testtool/busybox fdisk -l $1
/data/testtool/busybox fdisk -l $1 >> $log_patch/$project_name"_"$fun"_"$now.log &

sdinfo=`/data/testtool/busybox fdisk -l $1 |grep Disk | /data/testtool/busybox awk '{print $5}'`

		if [ -z  "$sdinfo" ] ; then
		Test_res=false
		echo "no usb card mounted" 
		echo "no usb card mounted" >> $log_patch/$project_name"_"$fun"_"$now.log &
		fi
else
   Test_res=false
   echo "No input USB1 device node"
   echo "No input USB1 device node" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi

if [ -n  "$2" ] ; then

/data/testtool/busybox fdisk -l $2
/data/testtool/busybox fdisk -l $2 >> $log_patch/$project_name"_"$fun"_"$now.log &

sdinfo=`/data/testtool/busybox fdisk -l $2 |grep Disk |/data/testtool/busybox awk '{print $5}'`

		if [ -z  "$sdinfo" ] ; then
		Test_res=false
		echo "no usb2 card mounted" 
		echo "no usb2 card mounted" >> $log_patch/$project_name"_"$fun"_"$now.log &
		fi
else
#   Test_res=false
   echo "No input USB2 device node"
   echo "No input USB2 device node" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi  

if [ -n  "$3" ] ; then

/data/testtool/busybox fdisk -l $3
/data/testtool/busybox fdisk -l $3 >> $log_patch/$project_name"_"$fun"_"$now.log &

sdinfo=`/data/testtool/busybox fdisk -l $3 |grep Disk |/data/testtool/busybox awk '{print $5}'`

		if [ -z  "$sdinfo" ] ; then
		Test_res=false
		echo "no usb3 card mounted" 
		echo "no usb3 card mounted" >> $log_patch/$project_name"_"$fun"_"$now.log &
		fi
else
#   Test_res=false
   echo "No input USB3 device node"
   echo "No input USB3 device node" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi  

if [ -n  "$4" ] ; then

/data/testtool/busybox fdisk -l $4
/data/testtool/busybox fdisk -l $4 >> $log_patch/$project_name"_"$fun"_"$now.log &

sdinfo=`/data/testtool/busybox fdisk -l $4 |grep Disk |/data/testtool/busybox awk '{print $5}'`

		if [ -z  "$sdinfo" ] ; then
		Test_res=false
		echo "no usb4 card mounted" 
		echo "no usb4 card mounted" >> $log_p1atch/$project_name"_"$fun"_"$now.log &
		fi
else
#   Test_res=false
   echo "No input USB4 device node"
   echo "No input USB4 device node" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 

echo 'Result:'
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish'
else
if [ "$TestMSG" != "" ] ; then
   echo "MSG: $TestMSG"
fi
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
if [ "$TestMSG" != "" ] ; then
   echo "MSG: $TestMSG" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi
if [ "$Test_res" == "true" ] ; then
   echo 'PASS' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
   echo 'FAIL' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
fi
echo 'Result end' >> $log_patch/$project_name"_"$fun"_"$now.log &
