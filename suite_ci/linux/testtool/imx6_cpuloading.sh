#!/bin/bash

#sample : ./imx6_cpuloading.sh [project_name] [cpu_loading] [test_time]
#project_name -> project name, ex: dms-ba38
#cpu_loading -> assign cpu loading percentage, ex:60
#test_time -> test time, ex:86400

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="cpu"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
        echo "Test Info :" >> $finallogPath
        if [ $(which stress-ng | wc -l) -le 0 ]; then
                echo "Without stress-ng test tool" >> $finallogPath
                testResult=1
        else
                stress-ng -c 0 -l $1 -t $2 &
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
