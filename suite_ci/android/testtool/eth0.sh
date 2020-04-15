OpenLoop=false
Test_res=true
TestMSG=" "
PINGHOST="www.hinet.net"

now="$(date +'%Y%m%d_%H%M%S')"
fun="ethernet"
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
echo 'Test_Item: ethernet'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: ethernet hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

svc wifi disable
busybox ifconfig eth0 up
sync
sleep 3
#netcfg   

MACaddress=`ifconfig eth0 | busybox awk 'NR==1{print $5}'`
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
    IP_ADDRESS=` ifconfig eth0 | busybox awk '/inet addr/{print substr($2,6)}'`
    netCount=$(($netCount+1))			
  done 
  echo $IP_ADDRESS
  echo $IP_ADDRESS >> $log_patch/$project_name"_"$fun"_"$now.log &
  
   if [ $(($netCount)) -lt 10 ] ; then
		PingData=""		
		PingData=`ping -c 5 $PINGHOST | grep time=`
		if [ "${PingData}" == "" ]; then
			 TestMSG="eth0 Ping test FAIL"
			 Test_res=false
		fi    		
  else
    TestMSG="eth0 get IP FAIL"
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
