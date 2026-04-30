@echo off
REM 哈夫曼编码系统 - Windows 编译脚本
REM 一键生成 .exe 文件

setlocal enabledelayedexpansion

echo.
echo ════════════════════════════════════════════════════════════
echo   哈夫曼编码系统编译器（Windows版本）
echo ════════════════════════════════════════════════════════════
echo.

REM 检查 g++ 是否存在
where g++ >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo ❌ 错误: 未找到 g++ 编译器
    echo.
    echo 解决方案:
    echo   1. 安装 MinGW: https://www.mingw-w64.org/
    echo   2. 或安装 Visual C++: https://visualstudio.microsoft.com/
    echo   3. 或使用在线编译: https://www.onlinegdb.com/
    echo.
    pause
    exit /b 1
)

echo ⏳ 正在编译 HuffmanSystem.cpp...
echo.

g++ -o HuffmanSystem.exe HuffmanSystem.cpp -std=c++11 -Wall

if %ERRORLEVEL% equ 0 (
    echo.
    echo ════════════════════════════════════════════════════════════
    echo ✅ 编译成功！
    echo ════════════════════════════════════════════════════════════
    echo.
    echo 文件已生成: HuffmanSystem.exe
    echo.
    echo 即将运行程序...
    echo.
    pause
    HuffmanSystem.exe
) else (
    echo.
    echo ========================================
    echo ❌ 编译失败
    echo ========================================
    echo.
    pause
    exit /b 1
)

endlocal
