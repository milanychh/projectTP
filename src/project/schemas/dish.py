from pydantic import BaseModel, Field, ConfigDict

class DishSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    dish_id: int
    dish_name: str
    description: str | None = Field(default=None)
