from pydantic import BaseModel, Field, ConfigDict

class MenuSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    menu_id: int
    dish_id: int
    recipe_id: int
    dish_name: str
    description: str | None = Field(default=None)
