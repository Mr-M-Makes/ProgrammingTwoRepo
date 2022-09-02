#Copy and paste this into powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
$mu = "https://github.com/mu-editor/mu/releases/download/v1.1.1/MuEditor-win64-1.1.1.msi"

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
#Download the file
Invoke-WebRequest -Uri $mu -OutFile "..\SetupNewComputer\Includes\mu.msi"
choco install arduino -y
choco install nodejs -y
choco install vcredist140  -y
choco install notepadplusplus.install -y
choco install python3 -y
choco install 7zip.install -y
choco install dotnetfx -y
choco install git.install -y
choco install vscode -y
choco install paint.net -y
choco install gimp -y
choco install inkscape -y
choco install slic3r -y
choco install cura-lulzbot -y
choco install openscad -y
choco install autodesk-fusion360 -y
choco install thonny -y


Get-Content extensions.list |% { code --install-extension $_}