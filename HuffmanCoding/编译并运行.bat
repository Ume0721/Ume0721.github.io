@echo off

echo ===== 哈夫曼编码系统编译脚本 =====
echo.

REM 检查g++是否存在
g++ --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [✓] 检测到g++编译器，开始编译...
    g++ -o HuffmanSystem.exe HuffmanSystem.cpp -std=c++11
    if %ERRORLEVEL% EQU 0 (
        echo.
        echo [✓] 编译成功！
        echo [✓] 已生成: HuffmanSystem.exe
        echo.
        echo 开始运行程序...
        echo.
        pause
        HuffmanSystem.exe
    ) else (
        echo [×] 编译失败，请检查代码或C++环境
        pause
    )
) else (
    echo [×] 未检测到g++编译器
    echo.
    echo 请按以下步骤安装：
    echo 1. 访问 https://www.mingw-w64.org/ 下载MinGW
    echo 2. 安装MinGW并添加到系统PATH
    echo 3. 重新运行此脚本
    echo.
    pause
)
