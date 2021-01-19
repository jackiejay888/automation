#!/bin/bash

#sample : ./imx6_cpu_info.sh [project_name]
#project_name -> project name, ex: dms-ba38

#arg and path
projectName="$1"
testTime=`date +%Y%m%d%H%M%S`
testFun="cpu_info"
logPath="/data/testtool"
testResult=0
finallogPath=$logPath/$projectName'_'$testFun'_'$testTime.log

#function
Test_Fun() {
        echo "Test Info :" >> $finallogPath
        if [ -e /proc/cpuinfo ]; then
                # check cpuinfo
                echo "[ CPU Info ]" >> $finallogPath
                cat /proc/cpuinfo >> $finallogPath
                echo " " >> $finallogPath
                # check cpufreq
                cpufreq_cnt=$(grep processor /proc/cpuinfo | wc -l)
                echo " [CPU Freq ]">> $finallogPath
                for ((i=0; i<$cpufreq_cnt; i++))
                do
                        cpufreq_min=$(cat /sys/devices/system/cpu/cpu$i/cpufreq/cpuinfo_min_freq)
                        cpufreq_max=$(cat /sys/devices/system/cpu/cpu$i/cpufreq/cpuinfo_max_freq)
                        cpufreq_cur=$(cat /sys/devices/system/cpu/cpu$i/cpufreq/cpuinfo_cur_freq)
                        echo "CPU$i" >> $finallogPath
                        echo "cpu freq min : $cpufreq_min" >> $finallogPath
                        echo "cpu freq max : $cpufreq_max" >> $finallogPath
                        echo "cpu freq cur : $cpufreq_cur" >> $finallogPath
                        echo " " >> $finallogPath
                done

        else
                echo "Without /proc/cpuinfo" >> $finallogPath
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


