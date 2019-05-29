D:
cd D:\code\automation\suite\roaming_cisco
del /f /q D:\code\automation\suite\roaming_cisco\wifi*.exe
copy dist\wifi_roaming_cisco.exe .\wifi_roaming_cisco.exe
del /f /q D:\code\automation\suite\roaming_cisco\*.log
del /f /q D:\code\automation\suite\roaming_cisco\*.txt
del /f /q D:\code\automation\suite\roaming_cisco\*.spec
del /f /q D:\code\automation\suite\roaming_cisco\*.pyc
rd /s /q D:\code\automation\suite\roaming_cisco\build
rd /s /q D:\code\automation\suite\roaming_cisco\dist
rd /s /q D:\code\automation\suite\roaming_cisco\__pycache__