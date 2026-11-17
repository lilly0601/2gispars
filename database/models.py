from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Business(Base):
    __tablename__ = "businesses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    business_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    subcategory: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    address: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    rating: Mapped[float] = mapped_column(
        Float,
        nullable=True
    )

    reviews_count: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="2gis"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        onupdate=datetime.now
    )

    parsed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )