OpenLoop=false
Test_res=false
TestMSG=" "

now="$(date +'%Y%m%d_%H%M%S')"
fun="backlight"
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
   echo 'Not support cpu'
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
   echo 'Not support android version'
#   exit 0
fi
fi 
fi
#check support android_version


#check support device

#check support device

echo 'MSG:'
echo 'Test_Item: backlight'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: backlight hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &



  Lvds_brightness_imx="/sys/devices/soc0/pwm-backlight/backlight/pwm-backlight/brightness"
  Lvds_brightness_rk="/sys/devices/platform/backlight/backlight/backlight/brightness"
  Lvds_brightness_x86="/sys/devices/pci0000:00/0000:00:02.0/drm/card0/card0-DSI-1/intel_backlight/brightness"

if [ "$cpu" == "imx6" ] ; then
  Lvds_brightness=$Lvds_brightness_imx
else
if [ "$cpu" == "rk3288" ] ; then
  Lvds_brightness=$Lvds_brightness_rk
else
if [ "$cpu" == "gmin" ] ; then
  Lvds_brightness=$Lvds_brightness_x86
fi 
fi 
fi

CURBrightness=0
brightness_test() {
	CURBrightness=$(cat $Lvds_brightness)
	#echo $CURBrightness
	loop1=0
	while [ $(($loop1)) -le 100 ];
	do
	    loop1=$(($loop1 +10))
		echo $loop1 > $Lvds_brightness
		#echo $loop1
		sleep 1
	done	
	echo $CURBrightness > $Lvds_brightness
	#echo $CURBrightness
}

brightness_test

if [ "$?" == "0" ] ; then
  Test_res=true
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

