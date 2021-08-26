@echo off
title Camera Trap GUI
echo.
echo [95m     /  _/   ____    _____  / /_  ____ _   / /   / /  ___    _____[0m 
echo [95m     / /    / __ \  / ___/ / __/ / __ `/  / /   / /  / _ \  / ___/[0m 
echo [95m   _/ /    / / / / (__  ) / /_  / /_/ /  / /   / /  /  __/ / /[0m     
echo [95m  /___/   /_/ /_/ /____/  \__/  \__,_/  /_/   /_/   \___/ /_/[0m
echo.                  
echo.
echo Installing Miniconda...
START /wait Miniconda3.exe /S /D=%~dp0..\Resources\Miniconda
echo [32mMiniconda installation complete![0m
echo.
echo Moving DLLs...
xcopy /q /y "%~dp0..\Resources\Miniconda\Library\bin\libcrypto-1_1-x64.dll" "%~dp0..\Resources\Miniconda\DLLs"
xcopy /q /y "%~dp0..\Resources\Miniconda\Library\bin\libssl-1_1-x64.dll" "%~dp0..\Resources\Miniconda\DLLs"
echo [32mDLLs Moved![0m
echo.
echo Creating Environment...
cd "%~dp0..\Resources\Miniconda\Scripts"
conda env create -q -f "%~dp0environment-gui.yml"
echo [32mEnvironment Installed![0m
echo [32mPackages Installed![0m
echo.
echo Activating environment...
CALL activate cameratraps-gui
echo [32mEnvironment Active![0m
echo.
echo Downloading Microsoft Dependencies...
curl https://github.com/microsoft/CameraTraps/archive/refs/heads/master.zip -L -o "%~dp0..\Resources\CameraTraps.zip"
curl https://github.com/microsoft/ai4eutils/archive/refs/heads/master.zip -L -o "%~dp0..\Resources\ai4eutils.zip"
curl https://lilablobssc.blob.core.windows.net/models/camera_traps/megadetector/md_v4.1.0/md_v4.1.0.pb -L -o "%~dp0..\Resources\md_v4.1.0.pb"
PowerShell.exe Expand-Archive -LiteralPath '%~dp0..\Resources\CameraTraps.zip' -DestinationPath '%~dp0..\Resources'
PowerShell.exe Expand-Archive -LiteralPath '%~dp0..\Resources\ai4eutils.zip' -DestinationPath '%~dp0..\Resources'
ren "%~dp0..\Resources\CameraTraps-master" CameraTraps
ren "%~dp0..\Resources\ai4eutils-master" ai4eutils
del "%~dp0..\Resources\CameraTraps.zip"
del "%~dp0..\Resources\ai4eutils.zip"
echo [32mMicrosoft Dependencies Downloaded![0
echo.
echo [32mInstallation Complete![0m
PAUSE