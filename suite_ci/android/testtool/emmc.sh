OpenLoop=false
Test_res=true
TestMSG=""
MountDisk="/data"
fifoStr="01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"


now="$(date +'%Y%m%d_%H%M%S')"
fun="storage_emmc"
project_name="usc130_a8"
log_patch="/data/testtool"

echo 'MSG:'
echo 'Test_Item: storage_emmc'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: storage_emmc hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

file_RW_test() {
	for i in { 0..$2 }
	do
	    touch "$1/test.txt"
		echo $fifoStr > "$1/test.txt"
		ReadStr=`cat $1/test.txt`
		#echo $ReadStr
		if [ "$fifoStr" != "$ReadStr" ]; then
		    TestMSG="$1 data miss"
			Test_res=false
		fi
		sleep 1
	done
}


file_RW_test $MountDisk 5	

echo 'Result:'
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish'
else
if [ "$TestMSG" != "" ] ; then
   echo "MSG: $TestMSG"
   echo "MSG: $TestMSG"  >> $log_patch/$project_name"_"$fun"_"$now.log &
fi
if [ "$Test_res" == "true" ] ; then
   echo 'PASS'
else
   echo 'FAIL'
fi 
fi
echo 'Result end'

echo 'Result:' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
if [ "$Test_res" == "true" ] ; then
   echo 'PASS' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
   echo 'FAIL' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
fi
echo 'Result end' >> $log_patch/$project_name"_"$fun"_"$now.log &

