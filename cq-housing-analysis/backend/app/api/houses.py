from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.house import House

router = APIRouter()


@router.get("/list")
async def list_houses(
    district: str | None = Query(default=None),
    min_price: float | None = Query(default=None),
    max_price: float | None = Query(default=None),
    layout: str | None = Query(default=None),
    sort_by: str = Query(default="crawled_at"),
    order: str = Query(default="desc"),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(House)

    if district:
        stmt = stmt.where(House.district == district)
    if min_price is not None:
        stmt = stmt.where(House.total_price >= min_price)
    if max_price is not None:
        stmt = stmt.where(House.total_price <= max_price)
    if layout:
        stmt = stmt.where(House.layout == layout)

    count_stmt = select(func.count()).select_from(stmt.subquery())
    total = (await db.execute(count_stmt)).scalar() or 0

    sort_col = getattr(House, sort_by, House.crawled_at)
    stmt = stmt.order_by(sort_col.desc() if order == "desc" else sort_col.asc())
    stmt = stmt.offset((page - 1) * page_size).limit(page_size)

    rows = (await db.execute(stmt)).scalars().all()

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "data": [
            {
                "id": h.id,
                "title": h.title,
                "district": h.district,
                "community": h.community,
                "total_price": h.total_price,
                "unit_price": h.unit_price,
                "area": h.area,
                "layout": h.layout,
                "floor": h.floor,
                "decoration": h.decoration,
                "building_year": h.building_year,
                "orientation": h.orientation,
                "tags": h.tags,
                "crawled_at": h.crawled_at.isoformat() if h.crawled_at else None,
            }
            for h in rows
        ],
    }


@router.get("/districts")
async def get_districts(db: AsyncSession = Depends(get_db)):
    stmt = select(House.district, func.count(House.id).label("count")).group_by(House.district)
    rows = (await db.execute(stmt)).all()
    return [{"district": r.district, "count": r.count} for r in rows]


@router.get("/summary")
async def get_summary(db: AsyncSession = Depends(get_db)):
    total = (await db.execute(select(func.count(House.id)))).scalar() or 0
    districts = (await db.execute(select(func.count(func.distinct(House.district))))).scalar() or 0
    avg_unit = (await db.execute(select(func.avg(House.unit_price)))).scalar() or 0
    avg_total = (await db.execute(select(func.avg(House.total_price)))).scalar() or 0

    return {
        "total_houses": total,
        "total_districts": districts,
        "avg_unit_price": round(float(avg_unit), 2),
        "avg_total_price": round(float(avg_total), 2),
    }
