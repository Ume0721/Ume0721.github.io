@echo off
REM Visual Studio CL编译器版本
REM 如果你安装了Visual Studio，可以使用此脚本

echo ===== 使用Visual Studio编译 =====
echo.

REM 检查Visual Studio编译器
cl.exe >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [✓] 检测到Visual Studio CL编译器
    cl.exe /o HuffmanSystem.exe HuffmanSystem.cpp
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo [✓] 编译成功！
        pause
        HuffmanSystem.exe
    ) else (
        echo [×] 编译失败
        pause
    )
) else (
    echo [×] 未检测到Visual Studio编译器
    echo.
    echo 请用 "编译并运行.bat" 脚本（使用MinGW编译器）
    echo 或者手动使用以下步骤：
    echo.
    echo 1. 打开 Visual Studio (或 Dev-C++)
    echo 2. 打开 HuffmanSystem.cpp 文件
    echo 3. 按 F11 或点击编译按钮
    echo.
    pause
)
