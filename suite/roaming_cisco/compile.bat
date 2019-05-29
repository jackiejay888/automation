D:
cd D:\code\automation\suite\roaming_cisco\
python -m py_compile wifi_roaming_cisco.py
copy __pycache__\wifi_roaming_cisco.cpython-36.pyc .\wifi_roaming_cisco.pyc
rd /s /q __pycache__