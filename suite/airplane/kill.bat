taskkill /f /im chromedriver.exe /t
taskkill /f /im python.exe /t
taskkill /f /im ping.exe /t
del /f /q D:\code\automation\suite\airplane\*.jpg
del /f /q D:\code\automation\suite\airplane\*.log
del /f /q D:\code\automation\suite\airplane\*.txt
del /f /q D:\code\automation\suite\airplane\*.spec
del /f /q D:\code\automation\suite\airplane\*.pyc
del /f /q D:\code\automation\suite\airplane\air*.exe
rd /s /q D:\code\automation\suite\airplane\build
rd /s /q D:\code\automation\suite\airplane\dist
rd /s /q D:\code\automation\suite\airplane\__pycache__