@rem to check if windows is 32 or 64 bit -- Paste in cmd

@echo off
py -c "import platform; print('Your system is', platform.architecture()[0])"
echo Press enter to exit
set /p input=
