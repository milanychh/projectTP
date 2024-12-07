from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class DiscountCardCreateUpdateSchema(BaseModel):
    discount_percentage: Decimal
    discount_conditions: str | None = Field(default=None)

class DiscountCardSchema(DiscountCardCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    discount_id: int
