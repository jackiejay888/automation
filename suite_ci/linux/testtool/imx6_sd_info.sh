#!/bin/bash

#sample : ./imx6_sd_info.sh [project_name]
#project_name -> project name, ex: dms-ba38

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="sd_info"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
        echo "Test Info :" >> $finallogPath
        if [ $(which fdisk | wc -l) -le 0 ]; then
                echo "Without fdisk test tool" >> $finallogPath
                testResult=1
        else
                fdisk -l /dev/mmcblk0 >> $finallogPath
                if [ $? -eq 1 ]; then
                        testResult=1
                        echo "Without mmcblk0 device" >> $finallogPath
                fi
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
