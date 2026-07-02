from datetime import datetime
from pydantic import BaseModel


class HouseOut(BaseModel):
    id: int
    title: str | None = None
    district: str
    community: str | None = None
    total_price: float | None = None
    unit_price: float | None = None
    area: float | None = None
    layout: str | None = None
    floor: str | None = None
    decoration: str | None = None
    building_year: int | None = None
    orientation: str | None = None
    tags: str | None = None
    crawled_at: datetime | None = None


class HouseListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    data: list[HouseOut]
