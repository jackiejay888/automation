D:
cd D:\code\automation\suite\roaming_cisco\
python -m py_compile roaming_cisco.py
copy __pycache__\roaming_cisco.cpython-36.pyc .\roaming_cisco.pyc
rd /s /q __pycache__