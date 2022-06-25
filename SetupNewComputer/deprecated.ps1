
#$UserPath = "$($env:USERPROFILE)\Desktop\InstallArduino.exe"
$arduino = "https://downloads.arduino.cc/arduino-1.8.19-windows.exe"

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Download the file
#Invoke-WebRequest -Uri $arduino -OutFile "..\SetupNewComputer\Includes\ard.exe"

$proc = Start-Process "..\SetupNewComputer\Deprecated_1st_run_in_Cmd.bat" -NoNewWindow -PassThru

# $proc = Start-Process "..\SetupNewComputer\Includes\Pystall.exe" -NoNewWindow -PassThru
# $proc.WaitForExit()
# $proc = Start-Process "..\SetupNewComputer\Includes\VSC.exe" -NoNewWindow -PassThru
# $proc.WaitForExit()
# Write-Output "Timeout is for 10 seconds"
# Timeout /T 10
# Write-Output "This line will be executed after 10 seconds if not interuptted"
# $proc = Start-Process "..\SetupNewComputer\Includes\ard.exe" -NoNewWindow -PassThru
# $proc.WaitForExit()
# Remove-Item '"..Includes\ard.exe"'
# echo "done"