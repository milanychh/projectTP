from pydantic import BaseModel, Field, ConfigDict

class MenuCreateUpdateSchema(BaseModel):
    dish_id: int
    recipe_id: int
    dish_name: str
    description: str | None = Field(default=None)

class MenuSchema(MenuCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    menu_id: int
