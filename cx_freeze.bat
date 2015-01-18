REM build using cx_freeze
c:\python34\python.exe setup.py build
REM try it
cd build
cd exe.win32-3.4
testcase.exe
cd ..
cd ..

