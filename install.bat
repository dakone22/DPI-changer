@echo off
cmd /c "cd /d venv\Scripts & activate & cd /d ..\.. & pip install --upgrade pip & pip install -r requirements.txt"
del install.bat