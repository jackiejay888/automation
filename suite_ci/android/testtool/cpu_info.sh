OpenLoop=false
Test_res=true
TestMSG=""
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="cpu_info"
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
echo 'Test_Item: cpu_info'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: cpu_info hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

Max_fps=$1
Min_fps=$2

sleep 10

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo3=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq" $cpuinfo3
echo "cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq" $cpuinfo3 >> $log_patch/$project_name"_"$fun"_"$now.log &


cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu5/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu5/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu5/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu7/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu7/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu7/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

		if [ $((cpuinfo3)) -gt $(($Min_fps)) ] ; then
		Test_res=false
		echo "CPU idle mode frequence too high:" $cpuinfo3 ">" $Min_fps
		echo "CPU idle mode frequence too high:" $cpuinfo3 ">" $Min_fps >> $log_patch/$project_name"_"$fun"_"$now.log &
		fi

/data/testtool/stress --cpu 4 --io 4 --vm 2 --vm-bytes 128M --timeout 10 >> $log_patch/$project_name"_"$fun"_"$now.log &

#delaysec=$(($1+3))

sleep 5

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo3=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq" $cpuinfo3
echo "cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq" $cpuinfo3 >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu4/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu5/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu5/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu5/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu6/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &

cpuinfo=`/data/testtool/busybox cat /sys/devices/system/cpu/cpu7/cpufreq/cpuinfo_cur_freq`
echo "cat /sys/devices/system/cpu/cpu7/cpufreq/cpuinfo_cur_freq" $cpuinfo
echo "cat /sys/devices/system/cpu/cpu7/cpufreq/cpuinfo_cur_freq" $cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &


		if [ $((cpuinfo3)) -lt $(($Max_fps)) ] ; then
		Test_res=false
		echo "CPU loading mode frequence too low:" $cpuinfo3 "<" $Max_fps
		echo "CPU loading mode frequence too low:" $cpuinfo3 "<" $Max_fps >> $log_patch/$project_name"_"$fun"_"$now.log &
		fi

/data/testtool/busybox cat /proc/cpuinfo
/data/testtool/busybox cat /proc/cpuinfo >> $log_patch/$project_name"_"$fun"_"$now.log &


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
