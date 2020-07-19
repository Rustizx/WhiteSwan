Invoke-WebRequest -OutFile create.zip http://whiteswan.blayone.com/create.zip
New-Item -ItemType directory -Path c:\temp
New-Item -ItemType directory -Path c:\temp\data
New-Item -ItemType directory -Path c:\temp\data\boot
Expand-Archive -Path create.zip -DestinationPath c:\temp\data\boot
Remove-Item -Path create.zip -Force
powershell -ExecutionPolicy ByPass -File c:\temp\data\boot\create\createWhiteSwan.ps1

