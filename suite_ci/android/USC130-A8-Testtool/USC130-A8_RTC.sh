OpenLoop=false
Test_res=true

echo 'MSG:'
echo 'Test_Item: RTC hardware'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

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
