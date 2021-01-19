#!/bin/bash

#sample : ./imx6_memory_tester.sh [project_name] [size] [loops]
#project_name -> project name, ex: dms-ba38
#size -> memory test size, ex: 100M
#loops -> test loops, ex: 1

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="memory_tester"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
	echo "Test Info :" >> $finallogPath
	if [ $(which memtester | wc -l) -le 0 ]; then			
		echo "Without memtester test tool" >> $finallogPath	
		return
	fi
	if [ ! $# -eq 1 ]; then
		echo "Please check input args ..." >> $finallogPath
		return
	fi
	if [ -e /tmp/memory.log ]; then
		rm /tmp/memory.log
	fi
	memtester $1 1 >> /tmp/memory.log
	cat /tmp/memory.log >> $finallogPath
	testResult=$(cat /tmp/memory.log | grep ok | wc -l)
	echo "$testResult"
	echo "Test is completed!!!" >> $finallogPath
}

Test_InitLog() {
	echo "MSG : " >> $finallogPath
	echo "Test_Item : $testFun" >> $finallogPath
	echo "Test Memory size : $1" >> $finallogPath
	echo "Test loop : 1" >> $finallogPath
	echo "MSG end" >> $finallogPath
}

Test_ResultLog() {
	echo "Result : " >> $finallogPath
	if [ $testResult -eq 16 ]; then	
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
