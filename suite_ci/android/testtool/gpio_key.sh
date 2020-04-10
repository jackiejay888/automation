OpenLoop=false
Test_res=true
TestMSG=""
MountDisk="/sys/devices/platform/gpio-keys/input"
fifoStr="01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="gpio_key"
project_name="usc130_a8"
log_patch="/data/testtool"

#check support device
if [ -n "$1" ] ; then

project_name=$1
#echo $project_name

else
project_name="trek734_a6"
#echo $project_name
fi

if [ "$project_name" == "trek734_a6" ] ; then
MountDisk="/sys/devices/soc0/soc/2100000.aips-bus/21a8000.i2c/i2c-2/2-0058/da9063-onkey/input"
  echo 'trek734_a6'
else
if [ "$project_name" == "usc130_a8" ] ; then
MountDisk="/sys/devices/platform/gpio-keys/input"
   echo 'usc130_a8'
else
   echo 'Not support project'
   exit 0
fi 
fi
#check support device

echo 'MSG:'
echo 'Test_Item: gpio_key'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: gpio_key hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

gpio_key_test() {
  for name in `ls $MountDisk`
	do

#echo $no_device
echo $1/$name
echo $1/$name >> $log_patch/$project_name"_"$fun"_"$now.log &
no_device=false
#echo $no_device


	done
}


gpio_key_test $MountDisk 5

if [ "$no_device" = "true" ] ; then
TestMSG="No gpio key"
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
