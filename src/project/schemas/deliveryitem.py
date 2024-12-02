from pydantic import BaseModel
from decimal import Decimal

class DeliveryItemSchema(BaseModel):
    item_id: int
    delivery_id: int
    product_id: int
    quantity: int
    unit_price: Decimal
