OpenLoop=false
Test_res=false
TestMSG=true
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="video_fps"
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
echo 'Test_Item: video_fps'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: video_fps hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

memtesterid=`ps -lA | grep "logcat"| busybox awk '{print $4}'`
kill $memtesterid

setprop debug.sf.fps 1
am start -a android.intent.action.VIEW -d file:////data/testtool/2160p_60fps.mp4 -t video/mp4
logcat -c ;logcat | grep mFps >> /data/testtool/video_fps.log  &
sleep 10
memtesterid=`ps -lA | grep "logcat"| busybox awk '{print $4}'`
kill $memtesterid
cat /data/testtool/video_fps.log |busybox awk '{print $9}' >> /data/testtool/video_fps2.log

while read line
do          

	echo $line| busybox awk 'BEGIN{FS="."} {print $1}' >> /data/testtool/video_fps3.log
	
done < /data/testtool/video_fps2.log


FILENAME=/data/testtool/video_fps3.log

Max_fps=0
Min_fps=30

while read line
do          
	if [ $(($line)) -gt "30" ] ; then
		#echo $line
		Test_res=true
		if [ $(($line)) -gt $(($Max_fps)) ] ; then
		Max_fps=$line
		#echo $Max_fps
		fi
	else
		#echo $Min_fps
		if [ $(($line)) -lt $(($Max_fps)) ] ; then
		Min_fps=$line
		#echo $Min_fps
		fi
    fi
	#echo $line| busybox awk 'BEGIN{FS="."} {print $1}' >>ttt.log
	
done < $FILENAME

rm /data/testtool/video_fps.log
rm /data/testtool/video_fps2.log
rm /data/testtool/video_fps3.log


echo 'Result:'
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish'
else
if [ "$TestMSG" != "" ] ; then
   echo "MSG: $TestMSG"
   echo "Max_fps: $Max_fps"
   echo "Min_fps: $Min_fps"
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
   echo "Max_fps: $Max_fps" >> $log_patch/$project_name"_"$fun"_"$now.log &
   echo "Min_fps: $Min_fps" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi
if [ "$Test_res" == "true" ] ; then
   echo 'PASS' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
   echo 'FAIL' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
fi
echo 'Result end' >> $log_patch/$project_name"_"$fun"_"$now.log &
