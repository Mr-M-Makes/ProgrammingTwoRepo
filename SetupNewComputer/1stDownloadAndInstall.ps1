#$UserPath = "$($env:USERPROFILE)\Desktop\InstallArduino.exe"
$arduino = "https://downloads.arduino.cc/arduino-1.8.19-windows.exe"

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Download the file
Invoke-WebRequest -Uri $arduino -OutFile "..\SetupNewComputer\Includes\ard.exe"

$proc = Start-Process "..\SetupNewComputer\Includes\Pystall.exe" -NoNewWindow -PassThru
$proc.WaitForExit()
$proc = Start-Process "..\SetupNewComputer\Includes\VSC.exe" -NoNewWindow -PassThru
$proc.WaitForExit()
$proc = Start-Process "..\SetupNewComputer\Includes\ard.exe" -NoNewWindow -PassThru
$proc.WaitForExit()
Remove-Item '"..\SetupNewComputer\Includes\ard.exe"'
echo "done"