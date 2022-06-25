
#$UserPath = "$($env:USERPROFILE)\Desktop\InstallArduino.exe"
$mu = "https://github.com/mu-editor/mu/releases/download/v1.1.1/MuEditor-win64-1.1.1.msi"

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Download the file
Invoke-WebRequest -Uri $arduino -OutFile "..\SetupNewComputer\Includes\mu.exe"



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