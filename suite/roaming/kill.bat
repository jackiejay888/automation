taskkill /f /im chromedriver.exe /t
taskkill /f /im python.exe /t
taskkill /f /im ping.exe /t
del /f /q D:\code\automation\suite\roaming\*.log
del /f /q D:\code\automation\suite\roaming\*.txt
del /f /q D:\code\automation\suite\roaming\*.spec
del /f /q D:\code\automation\suite\roaming\*.pyc
del /f /q D:\code\automation\suite\roaming\wifi*.exe
rd /s /q D:\code\automation\suite\roaming\build
rd /s /q D:\code\automation\suite\roaming\dist
rd /s /q D:\code\automation\suite\roaming\__pycache__