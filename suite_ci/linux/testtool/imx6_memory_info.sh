#!/bin/bash

#sample : ./imx6_memory_info.sh [project_name]
#project_name -> project name, ex: dms-ba38

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="memory_info"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
        echo "Test Info :" >> $finallogPath
        if [ -e /proc/meminfo ]; then
                cat /proc/meminfo >> $finallogPath
        else
                echo "Without /proc/meminfo" >> $finallogPath
                testResult=1
        fi
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
                echo "PASS" >> $finallogPath
        else
                echo "FAIL" >> $finallogPath
        fi
        echo "Result end" >> $finallogPath
}

#main
        Test_InitLog
        Test_Fun
        Test_ResultLog
