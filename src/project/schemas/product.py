from pydantic import BaseModel, Field, ConfigDict


class ProductCreateUpdateSchema(BaseModel):
    product_name: str
    expiry_date: str | None = Field(default=None)

class ProductSchema(ProductCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    product_id: int
