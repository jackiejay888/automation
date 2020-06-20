
OpenLoop=false
# Test_res=true
now="$(date +'%Y%m%d_%H%M%S')"
# now=$(date)
# echo 'OpenLoop'
# echo 'Test_res'
# echo 'now'
echo $now
echo $OpenLoop
if [ "$OpenLoop" == "false" ] ; then
  echo 'false'
else
  echo 'true'
fi