OpenLoop=false
Test_res=false
TestMSG=" "

now="$(date +'%Y%m%d_%H%M%S')"
fun="Audio_Speaker"
project_name="USC130_A8"
log_patch="/data/testtool"


echo 'MSG:'
echo 'Test_Item: Audio_Speaker'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: Audio_Speaker hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &


audio_Recode(){
tinymix 58 1
tinyplay /data/testtool/LRAudio.wav
}

if [ $(($AudioCount)) -lt 10 ] ; then

audio_Recode&
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

