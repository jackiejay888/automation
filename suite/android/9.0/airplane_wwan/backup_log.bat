@echo off

set nowYear=%date:~0,4%
set nowMonth=%date:~5,2%
set nowDay=%date:~8,2%
set nowHour=%time:~0,2%
set nowHour=%nowHour: =0%
set nowMinute=%time:~3,2%
set nowSecond=%time:~6,2%
set datetime=%nowYear%%nowMonth%%nowDay%_%nowHour%%nowMinute%%nowSecond%

md %datetime%

xcopy *.txt* %datetime%
xcopy *.log* %datetime%
xcopy *.jpg* %datetime%

move %datetime% ./backup/
