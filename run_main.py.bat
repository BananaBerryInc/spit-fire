@echo off

::If you have Python installed, this should work......
python main.py

:: This is where Johnnyw3 puts his files, so don't mind this
D:\Grade8\Utilities\Python\python.exe main.py
:: Drive might be mounted as e:\ for some reason...
E:\Grade8\Utilities\Python\python.exe main.py

::Drabtomato's files
E:\New_Folder\python.exe main.py
D:\New_Folder\python.exe main.py

set /p id="if you just got an error, type in the path to python.exe here:"

%id% main.py

::Sleep to see if there are errors in the code...
pause
