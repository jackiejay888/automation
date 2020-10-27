OpenLoop=false
Test_res=true
TestMSG=""
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="gpio_test"
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
   echo 'Not support cpu'
   exit 0
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
   echo 'Not support android version'
   exit 0
fi 
fi
fi
#check support android_version


#check support device

#check support device

echo 'MSG:'
echo 'Test_Item: gpio_test'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: gpio_test hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

numb=$1
list=$2

for n in $numb; do
   dire=`echo $n > /sys/class/gpio/export`
  done

 for n in $list; do
  echo "out" > /sys/class/gpio/$n/direction
  dire=`cat /sys/class/gpio/$n/direction`
  if [ x"$dire" != x"out" ]; then
     echo "$olist: directiont error!"
     echo "$olist: directiont error!" >> $log_patch/$project_name"_"$fun"_"$now.log &
     Test_res=1
  fi
 done


for n in $list;do
  echo 0 > /sys/class/gpio/$n/value
done
for n in $list;do
  val=`cat /sys/class/gpio/$n/value`
  if [ x"$val" != x"0" ];then
    echo "gpio:$n lo Test Fail"
    echo "gpio:$n lo Test Fail" >> $log_patch/$project_name"_"$fun"_"$now.log &
    Test_res=1 
   else 
        echo "gpio:$n lo Test PASS"
        echo "gpio:$n hi Test PASS" >> $log_patch/$project_name"_"$fun"_"$now.log &
  fi
done  


 
for n in $list;do
  dire=`cat /sys/class/gpio/$n/direction`
  val=`cat /sys/class/gpio/$n/value`
  echo "$n: $dire->$val"
  echo "$n: $dire->$val" >> $log_patch/$project_name"_"$fun"_"$now.log &

done

for n in $list;do
  echo 1 > /sys/class/gpio/$n/value
done
for n in $list;do
  val=`cat /sys/class/gpio/$n/value`
  if [ x"$val" != x"1" ];then
    echo "gpio:$n hi Test Fail"
    echo "gpio:$n hi Test Fail" >> $log_patch/$project_name"_"$fun"_"$now.log &
    Test_res=1 
    else 
        echo "gpio:$n hi Test PASS"
        echo "gpio:$n hi Test PASS" >> $log_patch/$project_name"_"$fun"_"$now.log &
  fi
done  


for n in $list;do
  dire=`cat /sys/class/gpio/$n/direction`
  val=`cat /sys/class/gpio/$n/value`
  echo "$n: $dire->$val"
  echo "$n: $dire->$val" >> $log_patch/$project_name"_"$fun"_"$now.log &

done

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
