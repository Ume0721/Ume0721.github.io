@echo off
chcp 65001 >nul
cls

title 哈夫曼编码演示系统 - 一键启动

echo.
echo ╔═══════════════════════════════════════════╗
echo ║     哈夫曼编码演示系统 - 智能启动管理     ║
echo ║          Huffman Coding Demo System        ║
echo ╚═══════════════════════════════════════════╝
echo.

setlocal enabledelayedexpansion

REM 检查HuffmanSystem.exe是否存在
if exist "HuffmanSystem.exe" (
    echo [√] 检测到编译好的程序: HuffmanSystem.exe
    echo.
    echo 选择操作：
    echo   1. 直接运行程序
    echo   2. 重新编译并运行
    echo   3. 查看源代码
    echo   0. 退出
    echo.
    set /p choice="请选择 (0-3): "

    if "!choice!"=="1" (
        echo.
        echo [√] 启动程序中...
        timeout /t 1 /nobreak >nul
        start HuffmanSystem.exe
        goto :end
    ) else if "!choice!"=="2" (
        goto :compile
    ) else if "!choice!"=="3" (
        echo.
        echo [√] 用记事本打开源代码...
        start notepad HuffmanSystem.cpp
        goto :end
    ) else (
        goto :end
    )
) else (
    echo [!] 未找到编译好的程序，进行自动编译...
    goto :compile
)

:compile
echo.
echo 检查编译工具...

REM 优先检查Visual Studio
if exist "%ProgramFiles%\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" (
    echo [√] 检测到 Visual Studio 2022
    call "%ProgramFiles%\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" >nul 2>&1
    echo [√] 开始编译...
    cl.exe /o HuffmanSystem.exe HuffmanSystem.cpp >nul 2>&1
    if !ERRORLEVEL! EQU 0 goto :runexe
)

REM 检查MinGW/gcc
where g++ >nul 2>&1
if !ERRORLEVEL! EQU 0 (
    echo [√] 检测到 MinGW (g++)
    echo [√] 开始编译...
    g++ -o HuffmanSystem.exe HuffmanSystem.cpp -std=c++11
    if !ERRORLEVEL! EQU 0 goto :runexe
)

REM 编译失败
echo.
echo [×] 编译失败！未检测到C++编译工具
echo.
echo 请选择以下选项之一：
echo.
echo 【选项 A】安装 MinGW (推荐)
echo   1. 访问: https://www.mingw-w64.org/
echo   2. 下载安装程序
echo   3. 安装时选择 "Add to PATH"
echo   4. 重新运行此脚本
echo.
echo 【选项 B】使用 Dev-C++
echo   1. 访问: https://www.bloodshed.net/
echo   2. 打开 HuffmanSystem.cpp
echo   3. 按 F11 编译运行
echo.
echo 【选项 C】使用在线编译器
echo   1. 访问: https://www.onlinegdb.com/
echo   2. 粘贴源代码
echo   3. 点击 Run
echo.
pause
goto :end

:runexe
echo.
echo ╔═══════════════════════════════════════════╗
echo ║           [√] 编译成功！                  ║
echo ║         即将启动程序...                    ║
echo ╚═══════════════════════════════════════════╝
echo.
timeout /t 2 /nobreak
HuffmanSystem.exe

:end
echo.
pause
