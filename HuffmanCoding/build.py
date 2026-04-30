#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
哈夫曼编码系统 - 编译脚本
编译 C++ 源代码为可执行文件
"""

import subprocess
import os
import sys
import platform

def compile_huffman():
    """编译 HuffmanSystem"""

    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    source = "HuffmanSystem.cpp"
    output = "HuffmanSystem.exe"

    print("=" * 60)
    print("💻 哈夫曼编码系统编译器")
    print("=" * 60)
    print(f"\n📁 工作目录: {script_dir}")
    print(f"📄 源文件: {source}")
    print(f"🎯 输出文件: {output}")
    print(f"🖥️  系统: {platform.system()}")
    print()

    # 检查源文件
    if not os.path.exists(source):
        print(f"❌ 错误: 找不到源文件 {source}")
        return False

    print("⏳ 正在编译...")

    try:
        # 编译命令
        cmd = ["g++", "-o", output, source, "-std=c++11", "-Wall"]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            print("✅ 编译成功！\n")

            # 显示文件大小
            if os.path.exists(output):
                size = os.path.getsize(output) / 1024  # 转换为 KB
                print(f"📊 文件大小: {size:.1f} KB")
                print(f"📍 完整路径: {os.path.abspath(output)}\n")

            print("=" * 60)
            print("✨ 编译完成！现在可以运行程序了")
            print("=" * 60)
            print("\n🚀 运行方式：")
            print(f"   • Windows: {output}")
            print(f"   • Linux/Mac: ./{output}")
            print()

            return True
        else:
            print(f"❌ 编译失败！\n错误输出:\n{result.stderr}")
            return False

    except FileNotFoundError:
        print("❌ 错误: 未找到 g++ 编译器")
        print("   请先安装 C++ 编译器:")
        print("   • Ubuntu/Debian: sudo apt-get install build-essential")
        print("   • macOS: brew install gcc")
        print("   • Windows: 安装 MinGW 或 Visual Studio")
        return False
    except subprocess.TimeoutExpired:
        print("❌ 错误: 编译超时")
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

if __name__ == "__main__":
    success = compile_huffman()
    sys.exit(0 if success else 1)
