
# [Serial Number]
# Read      : cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/serial_number
# Write      : echo 01234567890 > /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/serial_number 

# [Board Number]
# Read      : cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/board_number
# Write      : echo 01234567890 > /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/board_number 

# [HW Board ID]
# Read      : cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/board_id
# Write      : echo HIT-W101C-01 > /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/board_id 

# [Ethernet MAC]
# Read      : cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/eth_mac
# Write      : echo xx:xx:xx:xx:xx:xx > /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/eth_mac

#  不用  [WiFi MAC]
# Read      : cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/wifi_mac
# Write      : echo xx:xx:xx:xx:xx:xx > /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/wifi_mac 

# [BT MAC]
# Read      : cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/bt_mac
# Write      : echo xx:xx:xx:xx:xx:xx > /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/bt_mac

OpenLoop=false
Test_res=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="SystemInformation"
project_name="USC130_A8"
log_patch="/data/testtool"


echo 'MSG:'
echo 'Test_Item: system information'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: SystemInformation hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

svc wifi enable

#SerialNumb=`cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/serial_number`
#BoardNumber=`cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/board_number`
ModelNumber=`getprop ro.product.model`
if  [ "$ModelNumber" == "" ] ; 
then
  Test_res=false
  TestMSG="ModelNumber FAIL"
fi

AndroidVersion=`getprop ro.build.version.release`
if  [ "$AndroidVersion" == "" ] ; 
then
  Test_res=false
  TestMSG="AndroidVersion FAIL"
fi

BuildNumber=`getprop ro.build.display.id`
if  [ "$BuildNumber" == "" ] ; 
then
  Test_res=false
  TestMSG="BuildNumber FAIL"
fi

#Eth0Mac=`netcfg |grep eth0|awk '{print $5}'`
Eth0Mac=`ifconfig | grep eth0 | busybox  awk '{print $5}'`
if [ "$Eth0Mac" == "00:00:00:00:00:00" ] || [ "$Eth0Mac" == "FF:FF:FF:FF:FF:FF" ] || [ "$Eth0Mac" == "" ] ; 
then
  Test_res=false
  TestMSG="Eth0Mac FAIL"
fi

#wlan0Mac=`netcfg |grep wlan0|awk '{print $5}'`
wlan0Mac=`ifconfig | grep wlan0 | busybox  awk '{print $5}'`
if [ "$wlan0Mac" == "00:00:00:00:00:00" ] || [ "$wlan0Mac" == "FF:FF:FF:FF:FF:FF" ] || [ "$wlan0Mac" == "" ]; 
then
  Test_res=false
  TestMSG="wlan0Mac FAIL"
fi

#BTMAC=`settings get secure bluetooth_address`
#BTMAC=`cat /data/bluetooth/bt_mac`
SysMemorysize=`cat /proc/meminfo | grep MemTotal: | busybox awk '{print substr($2,0)}'`
eMMCFreeSpace=`df | grep /data/media | busybox awk '{print substr($2,0) }'`

	echo $project_name "System Information"
	echo -e "=============================================" 
#	echo "Serial Number : $SerialNumb"
#	echo "Board Number : $BoardNumber"
	echo "Model Number : $ModelNumber"

	echo "Android Version : $AndroidVersion"
	echo "BuildNumber : $BuildNumber"
	echo "Eth0 Mac Address : $Eth0Mac"	
    echo "wlan0 Mac Address : $wlan0Mac"	
#    echo "Bluetooth MAC Address: $BTMAC"
    echo "DDR3 Memory total size : $SysMemorysize (KB)"	
    echo "USER space : $eMMCFreeSpace"
	echo -e "=============================================" 

	echo $project_name "System Information" >> $log_patch/$project_name"_"$fun"_"$now.log &
	echo -e "=============================================" >> $log_patch/$project_name"_"$fun"_"$now.log &
#	echo "Serial Number : $SerialNumb" >> $log_patch/$project_name"_"$fun"_"$now.log &
#	echo "Board Number : $BoardNumber" >> $log_patch/$project_name"_"$fun"_"$now.log &
	echo "Model Number : $ModelNumber" >> $log_patch/$project_name"_"$fun"_"$now.log &

	echo "Android Version : $AndroidVersion" >> $log_patch/$project_name"_"$fun"_"$now.log &
	echo "BuildNumber : $BuildNumber" >> $log_patch/$project_name"_"$fun"_"$now.log &
	echo "Eth0 Mac Address : $Eth0Mac" >> $log_patch/$project_name"_"$fun"_"$now.log &
    echo "wlan0 Mac Address : $wlan0Mac" >> $log_patch/$project_name"_"$fun"_"$now.log &
#    echo "Bluetooth MAC Address: $BTMAC" >> $log_patch/$project_name"_"$fun"_"$now.log &
    echo "DDR3 Memory total size : $SysMemorysize (KB)"	>> $log_patch/$project_name"_"$fun"_"$now.log &
    echo "USER space : $eMMCFreeSpace" >> $log_patch/$project_name"_"$fun"_"$now.log &
	echo -e "============================================="  >> $log_patch/$project_name"_"$fun"_"$now.log &

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


