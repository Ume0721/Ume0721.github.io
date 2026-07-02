from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.house import House

router = APIRouter()


@router.get("/district-ranking")
async def get_district_ranking(db: AsyncSession = Depends(get_db)):
    stmt = (
        select(
            House.district,
            func.avg(House.unit_price).label("avg_price"),
            func.count(House.id).label("count"),
        )
        .group_by(House.district)
        .having(func.count(House.id) >= 10)
        .order_by(func.avg(House.unit_price).desc())
    )
    rows = (await db.execute(stmt)).all()
    return [{"district": r.district, "avg_price": round(float(r.avg_price), 0), "count": r.count} for r in rows]


@router.get("/price-trend")
async def get_price_trend(district: str | None = Query(default=None), db: AsyncSession = Depends(get_db)):
    stmt = select(
        func.strftime("%Y-%m", House.crawled_at).label("month"),
        func.avg(House.unit_price).label("avg_price"),
        func.count(House.id).label("count"),
    )
    if district:
        stmt = stmt.where(House.district == district)
    stmt = stmt.group_by("month").order_by("month")
    rows = (await db.execute(stmt)).all()
    return [{"month": r.month, "avg_price": round(float(r.avg_price), 0), "count": r.count} for r in rows if r.month]


@router.get("/layout-distribution")
async def get_layout_distribution(district: str | None = Query(default=None), db: AsyncSession = Depends(get_db)):
    stmt = select(House.layout, func.count(House.id).label("count")).where(House.layout.is_not(None))
    if district:
        stmt = stmt.where(House.district == district)
    stmt = stmt.group_by(House.layout).order_by(func.count(House.id).desc()).limit(10)
    rows = (await db.execute(stmt)).all()
    return [{"name": r.layout, "value": r.count} for r in rows]


@router.get("/scatter")
async def get_scatter(limit: int = Query(default=2000, le=5000), db: AsyncSession = Depends(get_db)):
    stmt = (
        select(House.area, House.total_price, House.district)
        .where(House.area.is_not(None), House.total_price.is_not(None))
        .order_by(func.random())
        .limit(limit)
    )
    rows = (await db.execute(stmt)).all()
    return [{"area": float(r.area), "price": float(r.total_price), "district": r.district} for r in rows]
