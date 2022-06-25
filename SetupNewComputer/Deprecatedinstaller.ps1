#Copy and paste this into powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

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

cat extensions.list |% { code --install-extension $_}