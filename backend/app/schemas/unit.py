
from pydantic import BaseModel, ConfigDict


class UnitBase(BaseModel):
    name: str
    abbreviation: str
    unit_type: str
    is_active: bool = True


class UnitCreate(UnitBase):
    pass


class UnitUpdate(BaseModel):
    name: str | None = None
    abbreviation: str | None = None
    unit_type: str | None = None
    is_active: bool | None = None


class UnitResponse(UnitBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
