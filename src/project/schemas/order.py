from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from decimal import Decimal


class OrderCreateUpdateSchema(BaseModel):
    client_id: int | None = Field(default=None)
    employee_id: int | None = Field(default=None)
    reservation_id: int | None = Field(default=None)
    discount_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    dish_id: int | None = Field(default=None)
    order_status: str | None = Field(default=None)
    total_price: Decimal | None = Field(default=None)


class OrderSchema(OrderCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    order_id: int
    order_datetime: datetime
