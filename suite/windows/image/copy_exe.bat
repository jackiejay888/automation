D:
cd D:\code\automation\suite\image
copy /Y dist\cv*.exe .
del /f /q *.log
del /f /q *.txt
del /f /q *.spec
#del /f /q *.pyc
rd /s /q build
rd /s /q dist
rd /s /q __pycache__
del /f /q *.jpg
