
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

#SerialNumb=`cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/serial_number`
#BoardNumber=`cat /sys/devices/soc0/soc.0/2000000.aips-bus/2000000.spba-bus/2008000.ecspi/spi_master/spi0/spi0.0/board_number`
ModelNumber=`getprop ro.product.model`
AndroidVersion=`getprop ro.build.version.release`
BuildNumber=`getprop ro.build.display.id`
#Eth0Mac=`netcfg |grep eth0|awk '{print $5}'`
Eth0Mac=`ifconfig | grep eth0 | busybox  awk '{print $5}'`
#wlan0Mac=`netcfg |grep wlan0|awk '{print $5}'`
wlan0Mac=`ifconfig | grep eth0 | busybox  awk '{print $5}'`
#BTMAC=`settings get secure bluetooth_address`
#BTMAC=`cat /data/bluetooth/bt_mac`
SysMemorysize=`cat /proc/meminfo | grep MemTotal: | busybox awk '{print substr($2,0)}'`
eMMCFreeSpace=`df | grep /data/media | busybox awk '{print substr($2,0) }'`

	echo "HIT-W101C System Information"
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
