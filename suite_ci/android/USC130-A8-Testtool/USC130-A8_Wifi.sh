OpenLoop=false
Test_res=true
TestMSG=" "
PINGHOST="www.hinet.net"


echo 'MSG:'
echo 'Test_Item: WIFI'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

svc wifi enable
busybox ifconfig eth0  down
sync
sleep 3
#netcfg   

MACaddress=`ifconfig wlan0 | busybox awk 'NR==1{print $5}'`
if [ "$MACaddress" == "00:00:00:00:00:00" ] || [ "$MACaddress" == "FF:FF:FF:FF:FF:FF" ] ; 
then
  Test_res=false
  TestMSG="MAC ID FAIL"
fi
echo $MACaddress

if [ "$MACaddress" == "" ];  then
   Test_res=false
   TestMSG="MAC ID FAIL"
fi

if [ "$Test_res" == "true" ] ; then
  IP_ADDRESS=""
  netCount=0
  while [ $(($netCount)) -le 10 ]&&[ "${IP_ADDRESS}" == "" ]
  do
     sleep 5
    IP_ADDRESS=` ifconfig wlan0 | busybox awk '/inet addr/{print substr($2,6)}'`
    netCount=$(($netCount+1))			
  done 
  echo $IP_ADDRESS
  
   if [ $(($netCount)) -lt 10 ] ; then
		PingData=""		
		PingData=`ping -c 5 $PINGHOST | grep time=`
		if [ "${PingData}" == "" ]; then
			 TestMSG="Wlan0 Ping test FAIL"
			 Test_res=false
		fi    		
  else
    TestMSG="Wlan0 get IP FAIL"
    Test_res=false
   fi 
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
