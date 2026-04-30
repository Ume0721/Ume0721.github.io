# Makefile for Huffman System
# 用法: make 或 make all (编译)
#       make run (运行)
#       make clean (清除编译文件)

CXX = g++
CXXFLAGS = -std=c++11 -Wall -O2
TARGET = HuffmanSystem.exe
SOURCE = HuffmanSystem.cpp

.PHONY: all run clean help

all: $(TARGET)

$(TARGET): $(SOURCE)
	@echo "⏳ 正在编译 $(SOURCE)..."
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCE)
	@echo "✅ 编译成功！生成文件: $(TARGET)"

run: $(TARGET)
	@echo "🚀 运行程序..."
	@./$(TARGET)

clean:
	@echo "🗑️  清除编译文件..."
	@rm -f $(TARGET)
	@echo "✓ 清除完成"

help:
	@echo "使用方式："
	@echo "  make         - 编译程序"
	@echo "  make run     - 编译并运行"
	@echo "  make clean   - 清除编译文件"
	@echo "  make help    - 显示帮助信息"
