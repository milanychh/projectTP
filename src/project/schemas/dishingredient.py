from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal


class DishIngredientCreateUpdateSchema(BaseModel):
    recipe_id: int
    product_id: int
    quantity: Decimal


class DishIngredientSchema(DishIngredientCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    record_id: int
