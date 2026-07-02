import pandas as pd
from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.house import House
from app.services.analyzer import HousingAnalyzer

router = APIRouter()


async def _load_dataframe(db: AsyncSession) -> pd.DataFrame:
    rows = (await db.execute(select(House))).scalars().all()
    data = [
        {
            "id": h.id,
            "district": h.district,
            "total_price": h.total_price,
            "unit_price": h.unit_price,
            "area": h.area,
            "layout": h.layout,
            "decoration": h.decoration,
            "building_year": h.building_year,
        }
        for h in rows
    ]
    return pd.DataFrame(data)


@router.get("/district-overview")
async def district_overview(db: AsyncSession = Depends(get_db)):
    df = await _load_dataframe(db)
    return [] if df.empty else HousingAnalyzer.district_overview(df)


@router.get("/prediction")
async def prediction(db: AsyncSession = Depends(get_db)):
    df = await _load_dataframe(db)
    return {"error": "无数据"} if df.empty else HousingAnalyzer.price_prediction(df)


@router.get("/clustering")
async def clustering(n_clusters: int = Query(default=5, ge=2, le=8), db: AsyncSession = Depends(get_db)):
    df = await _load_dataframe(db)
    return {"error": "无数据"} if df.empty else HousingAnalyzer.kmeans_clustering(df, n_clusters)


@router.get("/correlation")
async def correlation(db: AsyncSession = Depends(get_db)):
    df = await _load_dataframe(db)
    return {"error": "无数据"} if df.empty else HousingAnalyzer.correlation_analysis(df)
