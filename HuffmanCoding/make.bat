@echo off
cd /d "%~dp0"
g++ -o HuffmanSystem.exe HuffmanSystem.cpp -std=c++11
if errorlevel 1 (
    echo 编译失败
    pause
    exit /b 1
)
echo 编译成功！已生成 HuffmanSystem.exe
HuffmanSystem.exe
