from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class DeliveryCreateUpdateSchema(BaseModel):
    supplier_id: int
    delivery_date: Optional[str] = Field(default=None)

class DeliverySchema(DeliveryCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    delivery_id: int
