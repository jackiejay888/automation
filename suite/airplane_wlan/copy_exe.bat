D:
cd D:\code\automation\suite\airplane_wlan
copy /Y dist\airplane*.exe .
del /f /q D:\code\automation\suite\airplane_wlan\*.log
del /f /q D:\code\automation\suite\airplane_wlan\*.txt
del /f /q D:\code\automation\suite\airplane_wlan\*.spec
del /f /q D:\code\automation\suite\airplane_wlan\*.pyc
rd /s /q D:\code\automation\suite\airplane_wlan\build
rd /s /q D:\code\automation\suite\airplane_wlan\dist
rd /s /q D:\code\automation\suite\airplane_wlan\__pycache__
del /f /q D:\code\automation\suite\airplane_wlan\*.jpg