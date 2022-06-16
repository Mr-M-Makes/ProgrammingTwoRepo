$UserPath = "$($env:USERPROFILE)\Desktop\InstallArduino.exe"
$arduino = "https://downloads.arduino.cc/arduino-1.8.19-windows.exe"
$vscode = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64"
$py = "https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe"
$install = "\%UserProfile%\Desktop\InstallArduino.exe"
$installvs = "..\SetupNewComputer\Includes\VSC.exe"
$installpy = "..\SetupNewComputer\Includes\Pystall.exe"





[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Download the file
Invoke-WebRequest -Uri $arduino -OutFile $UserPath
echo "done"

#Invoke-WebRequest -Uri $vscode -OutFile $installvs
#echo "done"
#Invoke-WebRequest -Uri $py -OutFile $installpy
#echo "done"