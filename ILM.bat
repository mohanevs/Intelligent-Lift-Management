@echo off
title INTELLIGENT LIFT MANAGEMENT SYSTEM
color 0A

echo ================================================
echo    INTELLIGENT LIFT MANAGEMENT SYSTEM
echo    AI-Powered Priority-Based Elevator System
echo ================================================
echo.

:: Set paths
set ENV_PATH=C:\Users\ASUS\Desktop\CV_Projects\env
set BACKEND_PATH=C:\Users\ASUS\Desktop\CV_Projects\backend_v0.0.3

echo [1/3] Activating Python environment...
call "%ENV_PATH%\Scripts\activate.bat"
if errorlevel 1 (
    echo    [ERROR] Failed to activate environment!
    echo    Make sure environment exists at: %ENV_PATH%
    pause
    exit /b 1
)
echo    [OK] Environment activated!
echo.

echo [2/3] Starting Backend + Frontend Server...
start "Intelligent Lift Backend" cmd /k "cd /d "%BACKEND_PATH%" && call "%ENV_PATH%\Scripts\activate.bat" && python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000"
echo    Server starting on http://127.0.0.1:8000
echo.

:: Wait for server to initialize
timeout /t 3 /nobreak >nul

echo [3/3] Opening browser...
start http://127.0.0.1:8000

echo.
echo ================================================
echo    SYSTEM READY!
echo ================================================
echo    Server:  http://127.0.0.1:8000
echo    Home:    http://127.0.0.1:8000
echo ================================================
echo.
echo [INFO] The system is now running!
echo [INFO] Close the command windows to stop the servers.
echo.
pause