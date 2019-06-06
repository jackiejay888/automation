D:
cd D:\code\automation\suite\airplane_wwan
del /f /q D:\code\automation\suite\airplane_wwan\air*.exe
copy dist\airplane_wwan.exe .\airplane_wwan.exe
del /f /q D:\code\automation\suite\airplane_wwan\*.log
del /f /q D:\code\automation\suite\airplane_wwan\*.txt
del /f /q D:\code\automation\suite\airplane_wwan\*.spec
del /f /q D:\code\automation\suite\airplane_wwan\*.pyc
rd /s /q D:\code\automation\suite\airplane_wwan\build
rd /s /q D:\code\automation\suite\airplane_wwan\dist
rd /s /q D:\code\automation\suite\airplane_wwan\__pycache__
del /f /q D:\code\automation\suite\airplane_wwan\*.jpg