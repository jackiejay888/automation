D:
cd D:\code\automation\suite\roaming\
python -m py_compile wifi_roaming.py
copy __pycache__\wifi_roaming.cpython-36.pyc .\wifi_roaming.pyc
rd /s /q __pycache__