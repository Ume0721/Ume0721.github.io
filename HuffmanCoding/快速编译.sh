#!/usr/bin/env bash
# 哈夫曼系统编译脚本 - 跨平台版

cd "$(dirname "$0")"

echo "╔════════════════════════════════════════════╗"
echo "║   🔧 哈夫曼编码系统 - 跨平台编译器      ║"
echo "╚════════════════════════════════════════════╝"
echo ""

# 检查编译器
if ! command -v g++ &> /dev/null; then
    echo "❌ 错误：g++ 未找到"
    echo ""
    echo "请安装 C++ 编译器："
    echo "  Ubuntu/Debian: sudo apt-get install build-essential"
    echo "  macOS: brew install gcc"
    echo "  Windows: 安装 MinGW 或 Visual Studio"
    exit 1
fi

echo "✓ g++ 编译器就绪"
echo "📁 工作目录：$(pwd)"
echo ""
echo "⏳ 开始编译..."
echo ""

# 编译
g++ -o HuffmanSystem.exe HuffmanSystem.cpp -std=c++11 -O2

if [ $? -eq 0 ]; then
    echo ""
    echo "╔════════════════════════════════════════════╗"
    echo "║ ✅ 编译成功！HuffmanSystem.exe 已生成    ║"
    echo "╚════════════════════════════════════════════╝"
    echo ""

    # 显示文件信息
    ls -lh HuffmanSystem.exe
    echo ""
    echo "📍 文件位置：$(pwd)/HuffmanSystem.exe"
    echo ""
    echo "🚀 运行方式："
    echo "   • Linux/Mac: ./HuffmanSystem.exe"
    echo "   • Windows: HuffmanSystem.exe"
    echo ""

    # 询问是否立即运行
    read -p "现在运行程序吗？(y/n): " choice
    if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
        echo ""
        ./HuffmanSystem.exe
    fi
else
    echo ""
    echo "❌ 编译失败！"
    echo ""
    echo "排查步骤："
    echo "  1. 检查源文件 HuffmanSystem.cpp 是否存在"
    echo "  2. 检查 g++ 版本：g++ --version"
    echo "  3. 查看编译错误信息"
    exit 1
fi
