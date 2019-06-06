D:
cd D:\code\automation\suite\airplane_wlan
del /f /q D:\code\automation\suite\airplane_wlan\air*.exe
copy dist\airplane_wlan.exe .\airplane_wlan.exe
del /f /q D:\code\automation\suite\airplane_wlan\*.log
del /f /q D:\code\automation\suite\airplane_wlan\*.txt
del /f /q D:\code\automation\suite\airplane_wlan\*.spec
del /f /q D:\code\automation\suite\airplane_wlan\*.pyc
rd /s /q D:\code\automation\suite\airplane_wlan\build
rd /s /q D:\code\automation\suite\airplane_wlan\dist
rd /s /q D:\code\automation\suite\airplane_wlan\__pycache__
del /f /q D:\code\automation\suite\airplane_wlan\*.jpg