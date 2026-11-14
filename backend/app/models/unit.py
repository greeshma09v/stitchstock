
from sqlalchemy import Column, Integer, String, Boolean

from app.db.base import Base


class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), unique=True, nullable=False)

    abbreviation = Column(String(20), unique=True, nullable=False)

    unit_type = Column(String(30), nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
