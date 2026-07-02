from sqlalchemy import Date, DateTime, Float, Integer, String, Text, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class House(Base):
    __tablename__ = "houses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    source: Mapped[str] = mapped_column(String(20), default="mock")
    source_id: Mapped[str] = mapped_column(String(64))
    title: Mapped[str | None] = mapped_column(String(200), nullable=True)
    district: Mapped[str] = mapped_column(String(20))
    community: Mapped[str | None] = mapped_column(String(100), nullable=True)
    total_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    unit_price: Mapped[float | None] = mapped_column(Float, nullable=True)
    area: Mapped[float | None] = mapped_column(Float, nullable=True)
    layout: Mapped[str | None] = mapped_column(String(30), nullable=True)
    floor: Mapped[str | None] = mapped_column(String(50), nullable=True)
    orientation: Mapped[str | None] = mapped_column(String(20), nullable=True)
    decoration: Mapped[str | None] = mapped_column(String(20), nullable=True)
    building_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    tags: Mapped[str | None] = mapped_column(Text, nullable=True)
    listing_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    crawled_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    __table_args__ = (UniqueConstraint("source", "source_id", name="uq_source_source_id"),)
