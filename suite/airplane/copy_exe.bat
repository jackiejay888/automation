D:
cd D:\code\automation\suite\airplane
del /f /q D:\code\automation\suite\airplane\air*.exe
copy dist\airplane.exe .\airplane.exe
del /f /q D:\code\automation\suite\airplane\*.log
del /f /q D:\code\automation\suite\airplane\*.txt
del /f /q D:\code\automation\suite\airplane\*.spec
del /f /q D:\code\automation\suite\airplane\*.pyc
rd /s /q D:\code\automation\suite\airplane\build
rd /s /q D:\code\automation\suite\airplane\dist
rd /s /q D:\code\automation\suite\airplane\__pycache__
del /f /q D:\code\automation\suite\airplane\*.jpg