from pydantic import BaseModel
from decimal import Decimal
from pydantic import Field, ConfigDict

class DeliveryItemCreateUpdateSchema(BaseModel):
    delivery_id: int
    product_id: int
    quantity: int
    unit_price: Decimal

class DeliveryItemSchema(DeliveryItemCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    item_id: int
