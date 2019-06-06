taskkill /f /im chromedriver.exe /t
taskkill /f /im python.exe /t
taskkill /f /im ping.exe /t
del /f /q D:\code\automation\suite\airplane_wwan\*.jpg
del /f /q D:\code\automation\suite\airplane_wwan\*.log
del /f /q D:\code\automation\suite\airplane_wwan\*.txt
del /f /q D:\code\automation\suite\airplane_wwan\*.spec
del /f /q D:\code\automation\suite\airplane_wwan\*.pyc
del /f /q D:\code\automation\suite\airplane_wwan\air*.exe
rd /s /q D:\code\automation\suite\airplane_wwan\build
rd /s /q D:\code\automation\suite\airplane_wwan\dist
rd /s /q D:\code\automation\suite\airplane_wwan\__pycache__