OpenLoop=false
Test_res=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="RFID"
project_name="USC130_A8"
log_patch="/data/testtool"

echo 'MSG:'
echo 'Test_Item: RFID hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: RFID hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

lsusb | grep 10c4
#RFID = 'ls /dev/ttyUSB2'
RFID=`ls /dev/ttyUSB2 | busybox awk '{print substr($0,1)}'`
echo $RFID
echo $RFID >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ -z $RFID ] ; then
Test_res=false
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

