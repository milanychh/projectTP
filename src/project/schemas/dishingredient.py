from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class DishIngredientSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    record_id: int
    recipe_id: int
    product_id: int
    quantity: Decimal
