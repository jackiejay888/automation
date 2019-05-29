D:
cd D:\code\automation\suite\roaming
del /f /q D:\code\automation\suite\roaming\wifi*.exe
copy dist\wifi_roaming.exe .\wifi_roaming.exe
del /f /q D:\code\automation\suite\roaming\*.log
del /f /q D:\code\automation\suite\roaming\*.txt
del /f /q D:\code\automation\suite\roaming\*.spec
del /f /q D:\code\automation\suite\roaming\*.pyc
rd /s /q D:\code\automation\suite\roaming\build
rd /s /q D:\code\automation\suite\roaming\dist
rd /s /q D:\code\automation\suite\roaming\__pycache__