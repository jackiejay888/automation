OpenLoop=false
Test_res=true
TestMSG=""
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="display_info"
#project_name="usc130_a8"
project_name=`getprop ro.build.product`
#echo $project_name
#cpu="rk3288"
cpu=`getprop ro.board.platform`
#android_version="a8"
android_version=`getprop ro.build.version.release`
log_patch="/data/testtool"

diss_size=`wm size | grep "size:" | busybox awk {'print $3'}`
dis_density=`wm density | grep "density:" | busybox awk {'print $3'}`


#check support cpu

if [ "$cpu" == "rk3288" ] ; then
  echo 'rk3288'
else
if [ "$cpu" == "imx6" ] ; then
   echo 'imx6'
else
if [ "$cpu" == "gmin" ] ; then
   echo 'gmin'
else
   echo 'Not support cpu'
   exit 0
fi 
fi
fi
#check support cpu

#check support android_version

if [ "$android_version" == "8.1.0" ] ; then
  echo '8.1.0'
else
if [ "$android_version" == "6.0.0" ] ; then
   echo '6.0.0'
else
if [ "$android_version" == "6.0.1" ] ; then
   echo '6.0.1'
else
   echo 'Not support android version'
   exit 0
fi 
fi
fi
#check support android_version


#check support device

#check support device

echo 'MSG:'
echo 'Test_Item: display_info'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: display_info hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

sleep 1

    echo ' display size is '  $diss_size
    echo ' display size is '  $diss_size >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ "$diss_size" != "$1" ] ; then
  Test_res=false
  echo 'system display size is ' $diss_size but not $1
  echo 'system display size is ' $diss_size but not $1 >> $log_patch/$project_name"_"$fun"_"$now.log &

fi

  echo ' display density is '  $dis_density
  echo ' display density is '  $dis_density >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ "$dis_density" != "$2" ] ; then
  Test_res=false
  echo 'system display size is ' $dis_density but not $2
  echo 'system display size is ' $dis_density but not $2 >> $log_patch/$project_name"_"$fun"_"$now.log &

fi


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

echo 'Result:' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
  echo 'Finish' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
if [ "$TestMSG" != "" ] ; then
   echo "MSG: $TestMSG" >> $log_patch/$project_name"_"$fun"_"$now.log &
fi
if [ "$Test_res" == "true" ] ; then
   echo 'PASS' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
   echo 'FAIL' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
fi
echo 'Result end' >> $log_patch/$project_name"_"$fun"_"$now.log &
