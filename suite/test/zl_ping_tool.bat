::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJFqL8EcMKQ5AQwmDKGK1CIkP/eHv6taTp14JaPgzR5/S1LOxNO8c5gvhbZNN
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
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
