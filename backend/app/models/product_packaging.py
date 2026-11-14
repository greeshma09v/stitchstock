from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Numeric,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.db.base import Base


class ProductPackaging(Base):
    __tablename__ = "product_packaging"

    id = Column(Integer, primary_key=True, index=True)

    variant_id = Column(
        Integer,
        ForeignKey("product_variants.id"),
        nullable=False
    )

    package_name = Column(String(50), nullable=False)

    quantity_in_base_unit = Column(
        Numeric(12, 3),
        nullable=False
    )

    is_default = Column(Boolean, default=False, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)

    variant = relationship(
        "ProductVariant",
        back_populates="packaging_options"
    )