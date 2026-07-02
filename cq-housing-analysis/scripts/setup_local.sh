#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

cd "$ROOT_DIR"

echo "[1/4] 创建 Python 虚拟环境"
python3 -m venv .venv

source .venv/bin/activate

echo "[2/4] 升级 pip 并安装后端依赖"
pip install --upgrade pip
pip install -r backend/requirements.txt

echo "[3/4] 安装前端依赖"
cd frontend
npm install

cd "$ROOT_DIR"
echo "[4/4] 完成"
echo "后端启动: source .venv/bin/activate && cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo "前端启动: cd frontend && npm run dev -- --host 0.0.0.0 --port 5173"
