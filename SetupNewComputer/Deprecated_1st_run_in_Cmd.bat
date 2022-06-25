START %~dp0\Includes\node.msi
Pause
START %~dp0Includes\Pystall.exe
Pause
START %~dp0Includes\vsc.exe
Pause
START %~dp0\Includes\ard.exe
Pause
choco install arduino --version 1.8.19 -y
choco install vcredist140 --version 14.32.31326 -y
choco install notepadplusplus.install --version 8.4.2 -y
choco install python3 --version 3.10.5 -y
choco install 7zip.install --version 22.0 -y
choco install dotnetfx --version 4.8.0.20220524 -y
choco install git.install --version 2.36.1 -y
choco install vscode --version 1.68.1 -y
choco install paint.net --version 4.3.11 -y
choco install gimp --version 2.10.32.1 -y
choco install inkscape --version 1.2 -y
choco install slic3r --version 1.3.0 -y
choco install cura-lulzbot --version 3.6.37 -y
choco install openscad --version 2021.01 -y
choco install autodesk-fusion360 --version 2.0.13377 -y

