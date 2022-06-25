
#$UserPath = "$($env:USERPROFILE)\Desktop\InstallArduino.exe"
$mu = "https://github.com/mu-editor/mu/releases/download/v1.1.1/MuEditor-win64-1.1.1.msi"
$muinstall =  "$($env:USERPROFILE)\Desktop\mu.msi"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Download the file
Invoke-WebRequest -Uri $mu -OutFile $muinstall




Remove-Item '$muinstall'
echo "done"