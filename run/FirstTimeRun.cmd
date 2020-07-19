rmdir /s /q c:\temp\data\boot\create\
taskkill /F /IM powershell.exe
cd ..
start python\pythonw startClient.py
