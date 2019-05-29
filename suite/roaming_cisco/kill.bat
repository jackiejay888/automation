taskkill /f /im chromedriver.exe /t
taskkill /f /im python.exe /t
taskkill /f /im ping.exe /t
del /f /q D:\code\automation\suite\roaming_cisco\*.log
del /f /q D:\code\automation\suite\roaming_cisco\*.txt
del /f /q D:\code\automation\suite\roaming_cisco\*.spec
del /f /q D:\code\automation\suite\roaming_cisco\*.pyc
del /f /q D:\code\automation\suite\roaming_cisco\wifi*.exe
rd /s /q D:\code\automation\suite\roaming_cisco\build
rd /s /q D:\code\automation\suite\roaming_cisco\dist
rd /s /q D:\code\automation\suite\roaming_cisco\__pycache__