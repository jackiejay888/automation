OpenLoop=false
Test_res=true
TestMSG=" "
PINGHOST="www.hinet.net"

now="$(date +'%Y%m%d_%H%M%S')"
fun="wifi"
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
echo 'Test_Item: wifi'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: wifi hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

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
echo $MACaddress >> $log_patch/$project_name"_"$fun"_"$now.log &

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
  echo $IP_ADDRESS >> $log_patch/$project_name"_"$fun"_"$now.log &
  
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
