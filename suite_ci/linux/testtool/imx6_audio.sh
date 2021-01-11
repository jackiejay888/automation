#!/bin/bash

#sample : ./imx6_audio.sh [project_name]
#project_name -> project name, ex: dms-ba38

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="audio"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
	echo "Test Info :" >> $finallogPath
	if [ $(which amixer | wc -l) -le 0 ]; then			
		echo "Without amixer test tool" >> $finallogPath	
		return
	fi
        if [ $(which aplay | wc -l) -le 0 ]; then
                echo "Without aplay test tool" >> $finallogPath
                return
        fi
	
	echo "Test is completed!!!" >> $finallogPath
}

Test_InitLog() {
	echo "MSG : " >> $finallogPath
	echo "Test_Item : $testFun" >> $finallogPath
        echo "Test_Loading : $1 %" >> $finallogPath
        echo "Test_Time : $2 s" >> $finallogPath
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
	Test_InitLog $2 $3
	Test_Fun $2 $3
	Test_ResultLog
