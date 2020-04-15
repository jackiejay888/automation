OpenLoop=false
Test_res=false
TestMSG=" "

now="$(date +'%Y%m%d_%H%M%S')"
fun="audio_speaker"
project_name="usc130_a8"
cpu="rk3288"
android_version="a8"
log_patch="/data/testtool"

#check support cpu
if [ -n "$1" ] ; then

cpu=$1
#echo $project_name

else
cpu="rk3288"
#echo $project_name
fi

if [ "$cpu" == "rk3288" ] ; then
  echo 'rk3288'
else
if [ "$cpu" == "imx6" ] ; then
   echo 'imx6'
else
   echo 'Not support cpu'
   exit 0
fi 
fi
#check support cpu

#check support android_version
if [ -n "$2" ] ; then

android_version=$2
#echo $project_name

else
android_version="a8"
#echo $project_name
fi

if [ "$android_version" == "a8" ] ; then
  echo 'a8'
else
if [ "$android_version" == "a6" ] ; then
   echo 'a6'
else
   echo 'Not support cpu'
   exit 0
fi 
fi
#check support android_version

#check support device
if [ -n "$3" ] ; then

project_name=$3
#echo $project_name

else
project_name="usc130_a8"
#echo $project_name
fi

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
tinymix 58 1
tinyplay /data/testtool/LRAudio.wav
}

audio_Recode_imx(){
#tinymix 58 1
tinyplay /data/testtool/LRAudio.wav
}

if [ $(($AudioCount)) -lt 10 ] ; then

if [ "$cpu" == "imx6" ] ; then
  audio_Recode_imx&

else
if [ "$cpu" == "rk3288" ] ; then
  audio_Recode_rk&


fi 
fi

sleep 5
ProcessID=`ps|grep tinyplay |busybox awk '{print $2}'`
#echo  $ProcessID
kill -2 $ProcessID

if [ $(($ProcessID)) -gt 0 ] ; then
Test_res=true
fi

sleep 1

fi


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

