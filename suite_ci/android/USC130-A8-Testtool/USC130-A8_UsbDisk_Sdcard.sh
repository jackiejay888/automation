OpenLoop=false
Test_res=true
TestMSG=""
MountDisk="/mnt/media_rw"
fifoStr="01234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()"

echo 'MSG:'
echo 'Test_Item: Storage'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'


file_RW_test() {
  for name in `ls /mnt/media_rw`
	do
	    touch "$1/$name/test.txt"
		echo $fifoStr > "$1/$name/test.txt"
		ReadStr=`cat $1/$name/test.txt`
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
fi
if [ "$Test_res" == "true" ] ; then
   echo 'PASS'
else
   echo 'FAIL'
fi 
fi
echo 'Result end'
