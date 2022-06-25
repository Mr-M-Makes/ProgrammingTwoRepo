Powershell.exe -Command "& {Start-Process Powershell.exe -ArgumentList '-ExecutionPolicy Bypass -File %~dp0Installer.ps1' -Verb RunAs}"
Pause
START %~dp0Includes\Pystall.exe
