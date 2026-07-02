# 本地开发使用说明

## 1. 初始化环境

```bash
bash scripts/setup_local.sh
```

## 2. 启动后端

```bash
bash scripts/run_backend.sh
```

访问 API 文档:
- http://localhost:8000/api/docs

## 3. 启动前端

```bash
bash scripts/run_frontend.sh
```

访问前端:
- http://localhost:5173

## 4. 生成模拟数据

在前端数据浏览页点击"生成模拟数据"，或直接调用:

```bash
curl -X POST "http://localhost:8000/api/dataset/seed-mock?count=10000"
```
