from fastapi import APIRouter
from app.api import health, houses, visualization, statistics, dataset

api_router = APIRouter(prefix="/api")
api_router.include_router(health.router, tags=["健康检查"])
api_router.include_router(houses.router, prefix="/houses", tags=["房源"])
api_router.include_router(visualization.router, prefix="/viz", tags=["可视化"])
api_router.include_router(statistics.router, prefix="/stats", tags=["统计分析"])
api_router.include_router(dataset.router, prefix="/dataset", tags=["数据管理"])
