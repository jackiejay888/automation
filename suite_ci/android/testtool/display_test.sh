OpenLoop=false
Test_res=true
TestMSG=""
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="display_test"
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
echo 'Test_Item: display_test'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: display_test hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

sleep 1

show_pic(){

	am start -a android.intent.action.VIEW -d file:///data/testtool/LCD_Picture/$1 -t image/* &>/dev/null
}

panel_test() {
	for i in `ls /data/testtool/LCD_Picture/`;do
		show_pic $i
		#echo $i
		#echo $i  >> >> $log_patch/$project_name"_"$fun"_"$now.log &
		sleep 5
		ProcessID=`ps|grep com.android.gallery3d|awk '{print $2}'`    
        kill -2 $ProcessID

	done
	
	am start -a android.intent.action.MAIN -c android.intent.category.HOME
}

panel_test
sleep 5

am start -a android.intent.action.VIEW -d file:///data/testtool/2160p_60fps.mp4 -t video/mp4

		#echo "/data/testtool/2160p_60fps.mp4"
		#echo "/data/testtool/2160p_60fps.mp4"  >> $log_patch/$project_name"_"$fun"_"$now.log &

sleep 15

	am start -a android.intent.action.MAIN -c android.intent.category.HOME

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
