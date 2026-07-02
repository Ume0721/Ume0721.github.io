# 重庆市二手房价格分析系统（本地开发版）

这个版本已经完成主要项目内容的搭建，包括:
- FastAPI 后端接口
- Vue3 + Element Plus 前端页面
- 数据分析模块（预测 / 聚类 / 相关性）
- 模拟数据生成与清空接口

当前按你的要求，已跳过:
- 真实爬虫实现
- Docker Compose / Portainer
- 域名与公网发布配置


```

## 快速开始

```bash
cd cq-housing-analysis
bash scripts/setup_local.sh
```

启动后端:

```bash
bash scripts/run_backend.sh
```

启动前端:

```bash
bash scripts/run_frontend.sh
```

访问地址:
- 前端: http://localhost:5173
- API 文档: http://localhost:8000/api/docs
