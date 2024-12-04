from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class RecipeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    recipe_id: int
    dish_id: int
    product_id: int
    quantity: Decimal
