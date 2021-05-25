@REM Created on 2021/05/17

@REM @author: ZL Chen
@REM @title: Ping Tool

@echo off
@REM del log.csv
del zl_ping_tool.log
set /p ip_address=Please input the ip address or host name: 
@REM set ip_address=8.8.8.8
@REM set log="log.csv"
set log="zl_ping_tool.log"
echo Ping for windows environemnt. >> %log%
echo. >> %log%
@REM echo Date,Time,Status >> %log%
:top
@REM set nowDate=%date:~6,4%/%date:~0,2%/%date:~3,2%
set nowDate=%date:~0,20%
set nowHour=%time:~0,2%
set nowHour=%nowHour: =0%
set nowMinute=%time:~3,2%
set nowSecond=%time:~6,5%
set datetime=%nowDate% %nowHour%:%nowMinute%:%nowSecond%
@REM >>%log% set /p=%datetime% <nul&ping -n 1 %ip_address% | findstr "Reply from" >> %log%
@REM >>%log% echo %datetime%&ping -n 1 %ip_address% | findstr "Reply from" >> %log%
@REM >>%log% set /p=%datetime% <nul&ping -n 1 %ip_address% | findstr "Request timed out." >> %log%
>>%log% set /p=%datetime% <nul&ping -n 1 %ip_address% >> %log%
echo. >> %log%
@REM sleep 1
timeout /t 1
goto top
