from pydantic import BaseModel, Field, ConfigDict

class DeliverySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    delivery_id: int
    supplier_id: int
    delivery_date: str | None = Field(default=None)
