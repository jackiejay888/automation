OpenLoop=false
Test_res=false

now="$(date +'%Y%m%d_%H%M%S')"
fun="backlight"
project_name="usc130_a8"
log_patch="/data/testtool"

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

Lvds_brightness="/sys/devices/platform/backlight/backlight/backlight/brightness"
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

