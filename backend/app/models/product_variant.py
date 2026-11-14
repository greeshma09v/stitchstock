from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    color = Column(String(50), nullable=True)

    width = Column(String(50), nullable=True)

    size = Column(String(50), nullable=True)

    sku = Column(String(50), unique=True, nullable=True)

    is_active = Column(Boolean, default=True, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    product = relationship("Product", back_populates="variants")

    packaging_options = relationship(
      "ProductPackaging",
       back_populates="variant",
       cascade="all, delete-orphan"
)