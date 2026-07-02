from fastapi import APIRouter, Depends, Query
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.database import get_db
from app.models.house import House
from app.services.mock_data import generate_mock_records

router = APIRouter()


@router.post("/seed-mock")
async def seed_mock_data(count: int = Query(default=settings.MOCK_DEFAULT_COUNT, ge=100, le=100000), db: AsyncSession = Depends(get_db)):
    records = generate_mock_records(count)
    db.add_all([House(**item) for item in records])
    await db.commit()
    return {"message": "模拟数据生成完成", "count": count}


@router.delete("/clear")
async def clear_data(db: AsyncSession = Depends(get_db)):
    await db.execute(delete(House))
    await db.commit()
    return {"message": "数据已清空"}
