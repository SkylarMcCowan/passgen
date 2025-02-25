@echo off
:: Generate a 16-character complex password
setlocal EnableDelayedExpansion

:: Set the characters allowed in the password
set "chars=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?~"

:: Initialize the password variable
set "password="

:: Loop 16 times to generate the password
for /L %%i in (1,1,16) do (
    set /a rand=!random! %% 72
    set "password=!password!!chars:~!rand!,1!"
)

:: Output the generated password
echo Your generated password is: !password!

pause
