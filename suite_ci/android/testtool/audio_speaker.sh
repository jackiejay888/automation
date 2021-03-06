OpenLoop=false
Test_res=true
TestMSG=" "

now="$(date +'%Y%m%d_%H%M%S')"
fun="audio_speaker"
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
echo 'Test_Item: audio_speaker'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: audio_speaker hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &


audio_Recode_rk(){
#tinymix 58 1
#tinyplay /data/testtool/LRAudio.wav

am start -a android.intent.action.VIEW -d file:///data/testtool/LRAudio.wav -t video/wav

sleep 15
}

audio_Recode_imx(){
#tinymix 58 1
#tinyplay /data/testtool/LRAudio.wav
am start -a android.intent.action.VIEW -d file:///data/testtool/LRAudio.wav -t video/wav

sleep 15
}

#if [ $(($AudioCount)) -lt 10 ] ; then

#if [ "$cpu" == "imx6" ] ; then
#  audio_Recode_imx&

#else
#if [ "$cpu" == "rk3288" ] ; then
#  audio_Recode_rk&
audio_Recode_rk&
sleep 10

#fi 
#fi

#sleep 5
#ProcessID=`ps|grep tinyplay |/data/testtool/busybox awk '{print $2}'`
#echo  $ProcessID
#kill -2 $ProcessID

#if [ $(($ProcessID)) -gt 0 ] ; then
#Test_res=true
#fi

sleep 1

#fi


echo 'Result:'
if [ "$OpenLoop" == "true" ] ; then
     if [ "$TestMSG" != " "  ]; then
         echo "MSG: $TestMSG"
     fi 
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
   echo $TestMSG >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
fi
echo 'Result end' >> $log_patch/$project_name"_"$fun"_"$now.log &

