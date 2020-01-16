D:
cd D:\code\automation\suite_ci\roaming
del /f /q D:\code\automation\suite_ci\roaming\wifi*.exe
copy dist\wifi_roaming.exe .\wifi_roaming.exe
del /f /q D:\code\automation\suite_ci\roaming\*.log
del /f /q D:\code\automation\suite_ci\roaming\*.txt
del /f /q D:\code\automation\suite_ci\roaming\*.spec
del /f /q D:\code\automation\suite_ci\roaming\*.pyc
rd /s /q D:\code\automation\suite_ci\roaming\build
rd /s /q D:\code\automation\suite_ci\roaming\dist
rd /s /q D:\code\automation\suite_ci\roaming\__pycache__