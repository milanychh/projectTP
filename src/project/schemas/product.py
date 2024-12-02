from pydantic import BaseModel, Field, ConfigDict

class ProductSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
    product_name: str
    expiry_date: str | None = Field(default=None)
