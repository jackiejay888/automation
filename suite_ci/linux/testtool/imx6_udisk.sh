#!/bin/bash

#sample : ./imx6_udisk.sh [usb p1]
#usb p1 -> usb device part 1 , ex: sda1

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="Disk_RW"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log
fifoStr="01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

#function
Test_Fun() {
	echo "Test Info :" >> $finallogPath
	TMPDIR=`mktemp -d`
	if [[ ! -e "/dev/$1" ]]; then			
		echo "$1 : /dev/$1 no exist" >> $finallogPath	
		return
	fi
	sync&& umount "/dev/$1" &>/dev/null
	if `mount "/dev/$1" $TMPDIR &>/dev/null` ;then		
		echo $fifoStr > "$TMPDIR/test.txt"
		ReadStr=`cat $TMPDIR/test.txt`
		if [ $fifoStr == $ReadStr ]; then
			echo "$1 : Read/Write : [ Pass ]" >> $finallogPath
			testResult=1
		else
			echo "$1 : Read/Write : [ Fail ]" >> $finallogPath
			testResult=0
		fi
		sleep 1
		rm $TMPDIR/test.txt
		echo "Test is completed!!!" >> $finallogPath
		sync && umount "/dev/$1" &>/dev/null && sync && sleep 1
	else
		echo "$1 : /dev/$1 cannot be mounted correctly" >> $finallogPath	
		testResult=0
		echo "Test is completed!!!" >> $finallogPath
	fi
	rm -rf $TMPDIR
	echo "Test Info end" >> $finallogPath
}

Test_InitLog() {
	echo "MSG : " >> $finallogPath
	echo "Test_Item : $testFun" >> $finallogPath
	echo "Device : $1" >> $finallogPath
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
Test_InitLog $2
Test_Fun $2
Test_ResultLog


