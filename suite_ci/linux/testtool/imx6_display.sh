#!/bin/bash

#sample : ./imx6_display.sh [project_name]
#project_name -> project name, ex: dms-ba38

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="display"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
	echo "Test Info :" >> $finallogPath
	if [ $(which modetest | wc -l) -le 0 ]; then			
		echo "Without modetest test tool" >> $finallogPath	
		return
	fi
	modetest -c | grep 'id' >> $finallogPath
	modetest -c | grep -A 3 'connect' >> $finallogPath
	testResult=$(modetest -c | grep -w 'connected' | wc -l)
	echo "Test is completed!!!" >> $finallogPath
}

Test_InitLog() {
	echo "MSG : " >> $finallogPath
	echo "Test_Item : $testFun" >> $finallogPath
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
