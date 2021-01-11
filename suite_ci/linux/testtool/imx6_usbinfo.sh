#!/bin/bash

#sample : ./imx6_usbinfo.sh [project_name] [usb_device]
#project_name -> project name, ex: dms-ba38
#usb_device -> usb device, ex: sda

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="usb_info"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
	echo "Test Info :" >> $finallogPath
	fdisk -l /dev/$1 >> $finallogPath
	if [ $? -eq 1 ]; then
		testResult=1
	fi
	echo "Test is completed!!!" >> $finallogPath
}

Test_InitLog() {
	echo "MSG : " >> $finallogPath
	echo "Test_Item : $testFun" >> $finallogPath
	echo "Test Device : $1 " >> $finallogPath
	echo "MSG end" >> $finallogPath
}

Test_ResultLog() {
	echo "Result : " >> $finallogPath
	if [ $testResult -eq 0 ]; then	
		echo "PASS" >> $finallogPath
	else

		echo "FAIL" >> $finallogPath
	fi
	echo "Result end" >> $finallogPath
}

#main
	Test_InitLog $2
	Test_Fun $2
	Test_ResultLog
