@echo off
cmd /c "cd /d venv\Scripts & activate & pip install -r ..\..\requirements.txt"

mkdir IMAGES

attrib src +h
attrib venv +h
attrib .gitignore +h
attrib requirements.txt +h
attrib LICENSE +h

del install.bat