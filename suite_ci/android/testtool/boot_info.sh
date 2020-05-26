OpenLoop=false
Test_res=true
TestMSG=""
no_device=true

now="$(date +'%Y%m%d_%H%M%S')"
fun="boot_info"
#project_name="usc130_a8"
project_name=`getprop ro.build.product`
#echo $project_name
#cpu="rk3288"
cpu=`getprop ro.board.platform`
#android_version="a8"
android_version=`getprop ro.build.version.release`
log_patch="/data/testtool"



#check support cpu

if [ "$cpu" == "rk3288" ] ; then
  bootinfo=`getprop ro.boot.mode`
  echo 'rk3288'
else
if [ "$cpu" == "imx6" ] ; then
  bootinfo=`getprop ro.boot.storage_type`
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
echo 'Test_Item: boot_info'
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop'
else
echo ' test_type: CloseLoop'
fi 
echo 'MSG end'

echo 'MSG:' >> $log_patch/$project_name"_"$fun"_"$now.log
echo 'Test_Item: boot_info hardware' >> $log_patch/$project_name"_"$fun"_"$now.log &
if [ "$OpenLoop" == "true" ] ; then
echo ' test_type: OpenLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
else
echo ' test_type: CloseLoop' >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 
echo 'MSG end' >> $log_patch/$project_name"_"$fun"_"$now.log &

if [ "$bootinfo" != "emmc" ] ; then
  Test_res=false
  #echo $bootinfo
  echo 'system boot from' $bootinfo  'but not emmc'
  #echo $bootinfo >> $log_patch/$project_name"_"$fun"_"$now.log &
  echo 'system boot from' $bootinfo  'but not emmc' >> $log_patch/$project_name"_"$fun"_"$now.log &

else
  echo 'system boot from' $bootinfo
  echo 'system boot from' $bootinfo >> $log_patch/$project_name"_"$fun"_"$now.log &
fi 

hardware=`getprop ro.boot.hardware`
console=`getprop ro.boot.console`
selinux=`getprop ro.boot.selinux`
bincremental=`getprop ro.build.version.incremental`
breleasen=`getprop ro.build.version.release`
bsdk=`getprop ro.build.version.sdk`
btype=`getprop ro.build.type`
btype=`getprop ro.build.type`


echo ' ro.boot.hardware: ' $hardware
echo ' ro.boot.hardware: ' $hardware >> $log_patch/$project_name"_"$fun"_"$now.log &

echo ' ro.boot.console: '  $console 
echo ' ro.boot.console: '  $console  >> $log_patch/$project_name"_"$fun"_"$now.log &

echo ' ro.boot.selinux: '  $selinux
echo ' ro.boot.selinux: '  $selinux >> $log_patch/$project_name"_"$fun"_"$now.log &

echo ' ro.build.version.incremental: '  $bincremental
echo ' ro.build.version.incremental: '  $bincremental >> $log_patch/$project_name"_"$fun"_"$now.log &

echo ' ro.build.version.release: '  $breleasen
echo ' ro.build.version.release: '  $breleasen >> $log_patch/$project_name"_"$fun"_"$now.log &

echo ' ro.build.version.sdk: '  $bsdk
echo ' ro.build.version.sdk: '  $bsdk >> $log_patch/$project_name"_"$fun"_"$now.log &
  
echo ' ro.build.version.security_patch: '  $bsecurity_patch
echo ' ro.build.version.security_patch: '  $bsecurity_patch >> $log_patch/$project_name"_"$fun"_"$now.log &

echo ' ro.build.type: '  $btype
echo ' ro.build.type: '  $btype >> $log_patch/$project_name"_"$fun"_"$now.log &



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
