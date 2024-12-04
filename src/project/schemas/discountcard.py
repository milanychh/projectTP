from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class DiscountCardSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    discount_id: int
    discount_percentage: Decimal
    discount_conditions: str | None = Field(default=None)
