@echo off
@REM Mise en forme : HORODATAGE - MESSAGE
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

IF %1 EQU "" (
    set "message=%YYYY%/%MM%/%DD% %HH%:%Min%:%Sec% - Update"
) ELSE (
    set "message=%YYYY%/%MM%/%DD% %HH%:%Min%:%Sec% - %1"
)
echo %message%

@REM Push git
git add *
git commit -m "%message%"
git push