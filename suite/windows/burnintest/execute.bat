::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCuDJFqL8EcMKQ5AQwmDKGK1CIkP/eHv6taQq0MZW/UsRI3OyLqHLvQW+VHYdJI713ROncgEQhJbcXI=
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
::Zh4grVQjdCuDJFqL8EcMKQ5AQwmDKGK1CIkP/eHv6taQq0MZW/UsRI3OyLqHLvQW+VHYcI4o1W9OnfRdMxZRcFyudgpU
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
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
