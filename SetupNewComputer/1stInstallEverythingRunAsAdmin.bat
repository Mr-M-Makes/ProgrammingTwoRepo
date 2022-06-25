Powershell.exe -Command "& {Start-Process Powershell.exe -ArgumentList '-ExecutionPolicy Bypass -File %~dp01stRunInPowerShellAsAdmin.ps1' -Verb RunAs}"
Pause
START %~dp0Includes\Pystall.exe