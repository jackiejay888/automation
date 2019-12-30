..\bit.exe -c dqa.bitcfg -r -p -D 720

timeout 2

@echo off

set nowYear=%date:~10,4%
set nowMonth=%date:~4,2%
set nowDay=%date:~7,2%
set nowHour=%time:~0,2%
set nowHour=%nowHour: =0%
set nowMinute=%time:~3,2%
set nowSecond=%time:~6,2%
set datetime=%nowYear%%nowMonth%%nowDay%_%nowHour%%nowMinute%%nowSecond%

md %datetime%

xcopy /y C:\*BIT_log_*.htm %datetime%
xcopy /y C:\*BIT_log_*.log %datetime%

move %datetime% ./backup/
