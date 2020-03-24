OpenLoop=false
Test_res=false

echo 'MSG:'
echo 'Test_Item: Backlight'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

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





