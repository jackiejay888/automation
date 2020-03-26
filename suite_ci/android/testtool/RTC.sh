OpenLoop=false
Test_res=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="RTC"
project_name="USC130_A8"
log_patch="/data/testtool"

echo 'MSG:'
echo 'Test_Item: RTC hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: RTC hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

lsusb | grep 2394
lsusb | grep 2394 >> $log_patch/$project_name"_"$fun"_"$now.log &

date 080811352019.20
hwclock -w

# minunte check
Minunte=`hwclock -r | busybox awk '{print substr($4,4)}' | busybox cut -c 1-2 `
if [ $(($Minunte)) -ne 35 ] ; then
Test_res=false
fi

sleep 3
Seconds=`hwclock -r | busybox awk '{print substr($4,8)}'`

if [ $(($Seconds)) -lt 3 ]; then
Test_res=false
fi

if [ $(($Seconds)) -ge 6 ]; then
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

