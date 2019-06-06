taskkill /f /im chromedriver.exe /t
taskkill /f /im python.exe /t
taskkill /f /im ping.exe /t
del /f /q D:\code\automation\suite\airplane_wlan\*.jpg
del /f /q D:\code\automation\suite\airplane_wlan\*.log
del /f /q D:\code\automation\suite\airplane_wlan\*.txt
del /f /q D:\code\automation\suite\airplane_wlan\*.spec
del /f /q D:\code\automation\suite\airplane_wlan\*.pyc
del /f /q D:\code\automation\suite\airplane_wlan\air*.exe
rd /s /q D:\code\automation\suite\airplane_wlan\build
rd /s /q D:\code\automation\suite\airplane_wlan\dist
rd /s /q D:\code\automation\suite\airplane_wlan\__pycache__