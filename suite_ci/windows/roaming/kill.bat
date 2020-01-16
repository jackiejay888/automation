taskkill /f /im chromedriver.exe /t
taskkill /f /im python.exe /t
taskkill /f /im ping.exe /t
del /f /q D:\code\automation\suite_ci\roaming\*.log
del /f /q D:\code\automation\suite_ci\roaming\*.txt
del /f /q D:\code\automation\suite_ci\roaming\*.spec
del /f /q D:\code\automation\suite_ci\roaming\*.pyc
del /f /q D:\code\automation\suite_ci\roaming\wifi*.exe
rd /s /q D:\code\automation\suite_ci\roaming\build
rd /s /q D:\code\automation\suite_ci\roaming\dist
rd /s /q D:\code\automation\suite_ci\roaming\__pycache__