#!/bin/bash
# Linux/Mac版本编译脚本

cd "$(dirname "$0")"

echo "===== 哈夫曼编码系统编译脚本 ====="
echo ""

if command -v g++ &> /dev/null; then
    echo "[✓] 检测到g++编译器，开始编译..."
    g++ -o HuffmanSystem.exe HuffmanSystem.cpp -std=c++11

    if [ $? -eq 0 ]; then
        echo ""
        echo "[✓] 编译成功！"
        echo "[✓] 已生成: HuffmanSystem.exe"
        echo ""
        read -p "按Enter键运行程序..."
        ./HuffmanSystem.exe
    else
        echo "[×] 编译失败，请检查代码或C++环境"
    fi
else
    echo "[×] 未检测到g++编译器"
    echo ""
    echo "请在Linux上运行: sudo apt-get install build-essential"
    echo "或在Mac上运行: brew install gcc"
fi
