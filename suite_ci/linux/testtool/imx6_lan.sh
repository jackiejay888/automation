#!/bin/bash

#sample : ./imx6_lan.sh [project_name] [network_dev] [target_ip]
#project_name -> project name, ex: dms-ba38
#network_dev -> network device, ex: eth0
#target_ip -> test target ip address, ex: www.google.com

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="lan_ping"
logPath="/data/testtool"
testResult=0
pingResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log
fifoStr="01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

#function
Test_Fun() {
	echo "Test Info :" >> $finallogPath
	Net_dev=$(ifconfig $1)  
	if [ $? -eq 1 ]; then			
		echo "$1 device no exist" >> $finallogPath	
		return
	fi
	if [ -z $2 ]; then
		echo  "without target ip address" >> $finallogPath
		return
	fi
	pingResult=$(ping -I $1 -c 1 -W 3 $2 | grep loss | cut -f 7 -d ' ' | cut -f 1 -d '%')
	if [ $pingResult -eq 0 ]; then
		echo "$1 Ping test : [ Pass ]" >> $finallogPath
		testResult=1
	else
                echo "$1 Ping test : [ Fail ]" >> $finallogPath
                testResult=0
	fi
	echo "Test is completed!!!" >> $finallogPath
}

Test_InitLog() {
	echo "MSG : " >> $finallogPath
	echo "Test_Item : $testFun" >> $finallogPath
	echo "Device : $1" >> $finallogPath
	echo "IP : $(ifconfig eth0 | grep 'inet addr' | cut -f 2 -d : | cut -f 1 -d ' ')" >> $finallogPath
	echo "Target IP : $2" >> $finallogPath
	echo "MSG end" >> $finallogPath
}

Test_ResultLog() {
	echo "Result : " >> $finallogPath
	if [ $testResult -eq 0 ]; then	
		echo "FAIL" >> $finallogPath
	else
		echo "PASS" >> $finallogPath
	fi
	echo "Result end" >> $finallogPath
}

#main
	Test_InitLog $2 $3
	Test_Fun $2 $3
	Test_ResultLog
