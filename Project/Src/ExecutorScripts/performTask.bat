@echo off

set INSERT=INSERT
set UPDATE=UPDATE
set DELETE=DELETE
set RETRIEVE=RETRIEVE

set OPERATION=%1
set TASK_DETAILS=%2
set TASK_USER=%3
set TASK_DATE=%4

:: echo %OPERATION%
:: echo %INSERT%
:: echo %TASK_DETAILS%
:: echo %TASK_USER%
:: echo %TASK_DATE%

if %OPERATION% == %INSERT% (
        echo Insert equal
    ) else if %OPERATION% == %UPDATE% (
        echo Update Equal
    ) else if %OPERATION% == %DELETE% (
        echo Delete Equal
    ) else if %OPERATION% == %RETRIEVE% (
        echo RETRIEVE Equal
    ) else (
        echo Invalid OPERATION
    )