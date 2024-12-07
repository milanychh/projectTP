from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class RecipeCreateUpdateSchema(BaseModel):
    dish_id: int
    product_id: int
    quantity: Decimal

class RecipeSchema(RecipeCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    recipe_id: int
