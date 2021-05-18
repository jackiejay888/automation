#!/bin/bash

# @Created on 2021/05/18
# @Author: ZL Chen
# @Title: Ping Tool

# Sample: ./zl_ping_tool.sh "IP or Host Name"

# Definitino
file="zl_ping_tool.sh"
log="zl_ping_tool.log"

# Function
Ping_Initial() {
	rm -rf $log
	if [[ $1 != "" ]];
	then
	 	echo "IP address or Host name is: " $1
	else
		echo "No Argument."
		trap "echo BYE." EXIT
		killall $file
	fi
}

Ping() {
	Ping_Initial $1
	ip_address=$1
	while :
	do         
		datetime=`date +"%Y/%m/%d %H:%M:%T.%10N"`
		echo -e "\e[1;36mCurrent Time is: $datetime \e[0m" >> $log
		ping_log=`ping -c 1 "$ip_address"`
		echo -e "\e[1;33m$ping_log \e[0m" >> $log
		echo -e "\n" >> $log
		sleep 1
	done
}

# Main
	echo "Ping for windows environment."
	echo "Ping for windows environment." >> $log
	echo "You can tap the \"Ctrl+C\" button to interrupt the system."
	echo -n "Please input the ip address or host name: "
	read ip
	Ping $ip

