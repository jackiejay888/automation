OpenLoop=false
Test_res=true
TestMSG=""
MountDisk="/mnt/media_rw"
fifoStr="01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="usbdisk_sdcard"
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
echo 'Test_Item: usbdisk_sdcard'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: usbdisk_sdcard hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

test1=10

file_RW_test() {

END="$2"
echo $END
for i in $(seq 1 $END);
do
  for name in `ls /mnt/media_rw`
	do

#echo $no_device
echo $1/$name
echo $1/$name >> $log_patch/$project_name"_"$fun"_"$now.log &
no_device=false
#echo $no_device

	    touch "$1/$name/test.txt"
		echo $fifoStr > "$1/$name/test.txt"
		ReadStr=`cat $1/$name/test.txt`
		#echo $ReadStr
		echo $i: "PASS"
		echo $i: "PASS" >> $log_patch/$project_name"_"$fun"_"$now.log &
		if [ "$fifoStr" != "$ReadStr" ]; then
		    TestMSG="$1 data miss"
			Test_res=false
		echo $TestMSG
		echo $TestMSG >> $log_patch/$project_name"_"$fun"_"$now.log &
		fi
		sleep 1
	done
	done
}




file_RW_test $MountDisk $1	

if [ "$no_device" = "true" ] ; then
TestMSG="No media device"
Test_res=false
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
