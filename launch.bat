@echo off
echo.
echo ================================
echo   OrtoIoT-AI Dataset Creator
echo ================================
echo.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing/updating dependencies...
pip install -r requirements.txt

echo.
echo Starting OrtoIoT-AI...
python app.py

echo.
echo Application closed.
pause
