OpenLoop=false
Test_res=true
TestMSG=" "


now="$(date +'%Y%m%d_%H%M%S')"
fun="bluetooth"
project_name="usc130_a8"
log_patch="/data/testtool"


echo 'MSG:'
echo 'Test_Item: bluetooth'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: bluetooth hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

svc bluetooth disable
svc bluetooth enable

sleep 3
#netcfg   

MACaddress=`settings get secure bluetooth_address`
if [ "$MACaddress" == "00:00:00:00:00:00" ] || [ "$MACaddress" == "FF:FF:FF:FF:FF:FF" ] ; 
then
  Test_res=false
  TestMSG="MAC ID FAIL"
fi
echo $MACaddress
echo $MACaddress >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ "$MACaddress" == "" ];  then
   Test_res=false
   TestMSG="MAC ID FAIL"
fi


echo 'Result:'
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish'
else
if [ "$Test_res" == "true" ] ; then
   echo 'PASS'
else
   echo 'FAIL'
   echo $TestMSG
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
