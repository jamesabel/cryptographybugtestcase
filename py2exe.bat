REM build using py2exe
c:\python34\python.exe setup.py py2exe
REM try it
cd dist
testcase.exe
cd ..