@echo off

echo Creating virtual environment...
python -m venv venv

call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo Creating data folder...
if not exist data mkdir data

echo Setup complete.
pause
