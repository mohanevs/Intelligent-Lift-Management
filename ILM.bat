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
set FRONTEND_PATH=C:\Users\ASUS\Desktop\CV_Projects\frontend

echo [1/4] Activating Python environment...
call "%ENV_PATH%\Scripts\activate.bat"
if errorlevel 1 (
    echo    [ERROR] Failed to activate environment!
    echo    Make sure environment exists at: %ENV_PATH%
    pause
    exit /b 1
)
echo    [OK] Environment activated!
echo.

echo [2/4] Starting Backend Server...
start "Intelligent Lift Backend" cmd /k "cd /d "%BACKEND_PATH%" && call "%ENV_PATH%\Scripts\activate.bat" && python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000"
echo    Backend starting on http://127.0.0.1:8000
echo.

:: Wait for backend to initialize
timeout /t 3 /nobreak >nul

echo [3/4] Starting Frontend Server...
start "Intelligent Lift Frontend" cmd /k "cd /d "%FRONTEND_PATH%" && python -m http.server 3000"
echo    Frontend starting on http://127.0.0.1:3000
echo.

:: Wait for frontend to initialize
timeout /t 2 /nobreak >nul

echo [4/4] Opening browser...
start http://127.0.0.1:3000/home.html

echo.
echo ================================================
echo    SYSTEM READY!
echo ================================================
echo    Backend:  http://127.0.0.1:8000
echo    Frontend: http://127.0.0.1:3000
echo    Home:     http://127.0.0.1:3000/home.html
echo ================================================
echo.
echo [INFO] The system is now running!
echo [INFO] Close the command windows to stop the servers.
echo.
pause